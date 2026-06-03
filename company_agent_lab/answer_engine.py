from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PRODUCTS_PATH = ROOT / "data" / "sample_products.json"
ERP_PATH = ROOT / "data" / "sample_erp.json"


POWER_RE = re.compile(r"(\d{1,3})\s*(?:w|W|와트)")
IDENTIFIER_RE = re.compile(r"\b\d{8}\b")
MODEL_RE = re.compile(r"\bLUM-[A-Z0-9-]+\b", re.IGNORECASE)


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _normalize_light_color(text: str) -> str:
    lowered = text.lower()
    if any(token in lowered for token in ["웜화이트", "warm white", "3000k", "전구색"]):
        return "웜화이트"
    if any(token in lowered for token in ["쿨화이트", "cool white", "6000k", "6500k"]):
        return "쿨화이트"
    if any(token in lowered for token in ["주백색", "neutral white", "4000k", "4500k", "5000k"]):
        return "주백색"
    return ""


def _product_group_query(text: str) -> str:
    lowered = text.lower()
    if "볼라드" in text or "bollard" in lowered:
        return "bollard"
    if "태양광" in text or "solar" in lowered:
        return "solar"
    if "투광" in text or "flood" in lowered:
        return "flood"
    if "전기" in text or "electric" in lowered:
        return "electric"
    return ""


def _extract_power(text: str) -> str:
    match = POWER_RE.search(text)
    return f"{match.group(1)}W" if match else ""


def _wants_inventory(text: str) -> bool:
    return any(token in text for token in ["재고", "남았", "있나", "있는"])


def _wants_order(text: str) -> bool:
    return any(token in text for token in ["입고", "예정일", "납품", "발주"])


def _matches_product(product: dict[str, Any], query: str) -> bool:
    power = _extract_power(query)
    color = _normalize_light_color(query)
    group = _product_group_query(query)
    models = [item.upper() for item in MODEL_RE.findall(query)]
    identifiers = IDENTIFIER_RE.findall(query)

    if power and str(product.get("power", "")).upper() != power.upper():
        return False
    if color and str(product.get("light_color", "")) != color:
        return False
    if group and group not in product.get("product_group", []):
        return False
    if models and str(product.get("model", "")).upper() not in models:
        return False
    if identifiers and str(product.get("identifier", "")) not in identifiers:
        return False
    return bool(power or color or group or models or identifiers)


def _inventory_by_identifier(erp: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(item.get("identifier")): item for item in erp.get("inventory", [])}


def _render_products(matches: list[dict[str, Any]], erp: dict[str, Any], *, wants_inventory: bool) -> str:
    if not matches:
        return (
            "샘플 데이터에서 조건에 맞는 제품을 찾지 못했습니다.\n"
            "전력, 제품군, 광색, 모델명, 식별번호 중 어떤 기준으로 다시 찾을까요?"
        )

    inventory = _inventory_by_identifier(erp)
    lines = [f"샘플 데이터에서 {len(matches)}개 제품을 찾았습니다."]
    for product in matches:
        parts = [
            str(product.get("model", "")),
            f"식별번호 {product.get('identifier', '')}",
            str(product.get("power", "")),
            str(product.get("voltage", "")),
            f"광색 {product.get('light_color', '')}",
            f"가격 {product.get('price', 0):,}원",
            f"근거 {product.get('evidence', '')}",
        ]
        stock = inventory.get(str(product.get("identifier")))
        if wants_inventory:
            if stock:
                parts.append(f"현재고 {stock.get('stock', 0)}개")
                parts.append(f"상태 {stock.get('status', '')}")
            else:
                parts.append("현재고는 샘플 ERP 데이터에서 확인되지 않습니다")
        lines.append("- " + " | ".join(part for part in parts if part))
    lines.append("주의: 이 답변은 공개 실험판의 가짜 샘플 데이터 기준입니다.")
    return "\n".join(lines)


def _answer_order(query: str, erp: dict[str, Any]) -> str:
    hits: list[dict[str, Any]] = []
    for order in erp.get("orders", []):
        text = " ".join(
            [
                str(order.get("order_no", "")),
                str(order.get("customer", "")),
                str(order.get("project", "")),
                str(order.get("status", "")),
            ]
        )
        if any(token.lower() in text.lower() for token in query.split() if len(token) >= 2):
            hits.append(order)

    if not hits and "입고" in query:
        hits = list(erp.get("orders", []))

    if not hits:
        return (
            "샘플 ERP 데이터에서 관련 입고/발주 기록을 찾지 못했습니다.\n"
            "고객명, 프로젝트명, 모델명, 식별번호 중 어떤 기준으로 찾을까요?"
        )

    lines = [f"샘플 ERP 데이터에서 {len(hits)}개 입고/발주 기록을 찾았습니다."]
    for order in hits:
        date = order.get("expected_date") or order.get("received_date") or "확인 없음"
        lines.append(
            "- "
            + " | ".join(
                [
                    str(order.get("order_no", "")),
                    str(order.get("customer", "")),
                    str(order.get("project", "")),
                    f"상태 {order.get('status', '')}",
                    f"날짜 {date}",
                ]
            )
        )
    lines.append("주의: 이 답변은 공개 실험판의 가짜 ERP 데이터 기준입니다.")
    return "\n".join(lines)


def answer(query: str) -> dict[str, Any]:
    query = " ".join(str(query or "").split())
    if not query:
        return {"ok": False, "route": "empty", "answer": "질문을 입력해 주세요."}

    products = _load_json(PRODUCTS_PATH)
    erp = _load_json(ERP_PATH)

    if _wants_order(query):
        return {"ok": True, "route": "erp_order", "answer": _answer_order(query, erp)}

    matches = [product for product in products if _matches_product(product, query)]
    return {
        "ok": True,
        "route": "product_search",
        "answer": _render_products(matches, erp, wants_inventory=_wants_inventory(query)),
        "match_count": len(matches),
    }
