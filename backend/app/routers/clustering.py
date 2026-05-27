from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from ..database import get_db

from RagBot.app.cluster.cluster_skill import (run_clustering)

router = APIRouter(
    prefix="/api/clustering",
    tags=["Clustering"]
)


@router.post("/run")
def cluster_users(
    db: Session = Depends(get_db)
):

    results = run_clustering(db)

    return {
        "clusters": results
    }