from datetime import datetime, timezone
from threading import Lock
from uuid import uuid4

from fastapi import FastAPI

from relay_api.schemas.ticket_create import CreateTicketRequest
from relay_api.schemas.ticket_response import TicketResponse

app = FastAPI()
app.state.tickets = []
app.state.ticket_lock = Lock()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/tickets", status_code=201)
def create_ticket(request: CreateTicketRequest) -> TicketResponse:
    ticket = TicketResponse(
        id=uuid4(),
        title=request.title,
        priority=request.priority,
        created_at=datetime.now(timezone.utc),
    )
    with app.state.ticket_lock:
        app.state.tickets.append(ticket)
    return ticket


@app.get("/tickets", response_model=list[TicketResponse])
def list_tickets() -> list[TicketResponse]:
    with app.state.ticket_lock:
        return list(app.state.tickets)