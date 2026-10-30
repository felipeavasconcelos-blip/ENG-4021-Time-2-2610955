import datetime
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

permissoes = ["https://www.googleapis.com/auth/calendar.readonly"]
credenciais = None

if os.path.exists("token.json"):
    credenciais = Credentials.from_authorized_user_file(
        "token.json",
        permissoes
    )

if not credenciais or not credenciais.valid:
    if credenciais and credenciais.expired and credenciais.refresh_token:
        credenciais.refresh(Request())
    else:
        fluxo = InstalledAppFlow.from_client_secrets_file(
            "credentials.json",
            permissoes
        )
        credenciais = fluxo.run_local_server(port=0)

    with open("token.json", "w") as arquivo:
        arquivo.write(credenciais.to_json())

calendar = build("calendar", "v3", credentials=credenciais)

agora = datetime.datetime.now(
    tz=datetime.timezone.utc
).isoformat()

resultado = calendar.events().list(
    calendarId="primary",
    timeMin=agora,
    maxResults=10,
    singleEvents=True,
    orderBy="startTime"
).execute()

eventos = resultado.get("items", [])

if not eventos:
    print("Nenhum evento futuro foi encontrado.")
else:
    print("Próximos eventos:")

    for evento in eventos:
        inicio = evento["start"].get(
            "dateTime",
            evento["start"].get("date")
        )
        print(inicio, evento["summary"])
        