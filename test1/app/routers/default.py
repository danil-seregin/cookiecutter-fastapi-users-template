from fastapi import APIRouter, Request

router = APIRouter()


@router.api_route("/test-webhook", methods=["GET", "POST", "PUT", "DELETE", "PATCH"], tags=["Default"])
async def test_webhook(request: Request):
    """
    Универсальный тестовый вебхук: принимает любые методы и данные, печатает их.
    """
    try:
        body = await request.json()
    except Exception:
        body = await request.body()  # если не JSON, получаем raw bytes

    print(f"Received request to {request.url}")
    print(f"Method: {request.method}")
    print(f"Headers: {dict(request.headers)}")
    print(f"Body: {body}")

    return {"status": "ok", "message": "Request received"}