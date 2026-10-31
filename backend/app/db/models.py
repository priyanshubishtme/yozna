from datetime import datetime, UTC
from sqlalchemy import String, Integer, DateTime, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Source(Base):
    __tablename__ = "sources"
    source_id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    base_url: Mapped[str] = mapped_column(String)
    source_family: Mapped[str] = mapped_column(String)
    permission_status: Mapped[str] = mapped_column(String, default="pending_review")
    automation_status: Mapped[str] = mapped_column(String, default="disabled")
    schedule_cron: Mapped[str] = mapped_column(String, nullable=True)

class Scheme(Base):
    __tablename__ = "schemes"
    scheme_id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    jurisdiction: Mapped[str] = mapped_column(String)
    rag_enabled: Mapped[bool] = mapped_column(Boolean, default=False)
    rules_enabled: Mapped[bool] = mapped_column(Boolean, default=False)

class Document(Base):
    __tablename__ = "documents"
    document_id: Mapped[str] = mapped_column(String, primary_key=True)
    scheme_id: Mapped[str] = mapped_column(String, nullable=True)
    status: Mapped[str] = mapped_column(String) # verified, pending_review

class DocumentVersion(Base):
    __tablename__ = "document_versions"
    version_id: Mapped[str] = mapped_column(String, primary_key=True)
    document_id: Mapped[str] = mapped_column(String)
    binary_sha256: Mapped[str] = mapped_column(String)
    content_type: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC))
