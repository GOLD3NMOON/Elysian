import os
import dotenv
dotenv.load_dotenv()

settings = {
  "TOKEN": str(os.getenv("TOKEN")),
  "PREFIX": "!",
}
