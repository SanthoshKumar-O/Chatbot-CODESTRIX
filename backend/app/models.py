import uuid
from sqlalchemy import Column, Date, String, Text, ForeignKey, DateTime, Integer, Float
from sqlalchemy.dialects.postgresql import JSON, UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    sessions = relationship("Session", back_populates="owner", cascade="all, delete-orphan")

class Session(Base):
    __tablename__ = "sessions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
    title = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    owner = relationship("User", back_populates="sessions")
    messages = relationship("Message", back_populates="session", cascade="all, delete-orphan")

class Message(Base):
    __tablename__ = "messages"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    session_id = Column(UUID(as_uuid=True), ForeignKey("sessions.id", ondelete="CASCADE"))
    role = Column(String, nullable=False) # 'user' or 'assistant'
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    session = relationship("Session", back_populates="messages")

class QuizAttempt(Base):

    __tablename__ = "quiz_attempts"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True
    )

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE")
    )
    topic = Column(String, nullable=False)
    questions = Column(JSON)
    results = Column(JSON)
    difficulty = Column(String, nullable=False)
    score = Column(Integer, nullable=False)
    total_questions = Column(Integer, nullable=False)
    accuracy = Column(Float, nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    user = relationship("User")

class UserProfile(Base):

    __tablename__ = "user_profiles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True
    )
    average_quiz_score = Column(Float, default=0)
    quizzes_taken = Column(Integer, default=0)
    study_consistency = Column(Float, default=0)
    learning_behavior = Column(String, default="balanced")
    days_active = Column(Integer, default=0)
    total_sessions = Column(Integer, default=0)
    current_streak = Column(Integer, default=0)
    total_messages = Column(Integer, default=0)
    last_active_date = Column(Date, nullable=True)
    quizzes_taken = Column(Integer, default=0)
    average_quiz_score = Column(Float, default=0)
    teaching_requests = Column(Integer, default=0)
    quiz_requests = Column(Integer, default=0)
    preferred_topic = Column(String, nullable=True)
    average_message_length = Column(Float, default=0)
    

class TopicPerformance(Base):

    __tablename__ = "topic_performance"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE")
    )

    topic = Column(String, nullable=False)

    average_score = Column(Float, default=0)

    quizzes_taken = Column(Integer, default=0)

    last_score = Column(Float, default=0)