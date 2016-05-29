import os
from sqlalchemy import create_engine
from schedule.models import Model


if __name__ == "__main__":
    engine = create_engine(os.environ['DATABASE_URL'])
    Model.metadata.create_all(engine)
