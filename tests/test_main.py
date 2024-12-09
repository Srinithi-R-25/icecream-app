import sys
import os
import pytest
from sqlalchemy.orm import Session
from app.models import SessionLocal, Flavor

# Test function to add a flavor to the database
def test_add_flavor():
    # Create a new session
    db: Session = SessionLocal()

    # Add a new flavor
    new_flavor = Flavor(name="Vanilla", ingredients="Milk, Sugar")
    db.add(new_flavor)
    db.commit()

    # Query the database to check if the flavor exists
    flavor = db.query(Flavor).filter_by(name="Vanilla").first()
    assert flavor is not None
    assert flavor.name == "Vanilla"
    assert flavor.ingredients == "Milk, Sugar"

    # Clean up the test data
    db.delete(flavor)
    db.commit()

    # Close the session
    db.close()
