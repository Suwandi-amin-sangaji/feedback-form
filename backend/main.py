from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

# Koneksi ke database PostgreSQL
DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost/db_test"
engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer)

Base.metadata.create_all(bind=engine)

class FeedbackCreate(BaseModel):
    rating: int

@app.post("/api/feedback/")
def create_feedback(feedback: FeedbackCreate):
    try:
        db = SessionLocal()
        db_feedback = Feedback(rating=feedback.rating)
        db.add(db_feedback)
        db.commit()
        db.refresh(db_feedback)
        db.close()
        return {"success": True}  # Mengembalikan respons yang sesuai setelah berhasil disimpan
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
