import click
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.model import Base, Band, Venue, Concert  # Adjusted for your project structure

# Create an engine and bind it to the session
engine = create_engine('sqlite:///concerts.db')  # Change to your preferred database URL
Base.metadata.create_all(engine)  # Create tables if they don't exist
Session = sessionmaker(bind=engine)

@click.group()
def cli():
    """Concert Management CLI."""
    click.echo("Welcome to the Concert Management CLI!")

@cli.command()
@click.argument('name')
@click.argument('hometown')
def create_band(name, hometown):
    """Create a new band."""
    session = Session()  # Create a new session
    try:
        band = Band(name=name, hometown=hometown)
        session.add(band)
        session.commit()
        click.echo(f"Band '{name}' created successfully.")
    except Exception as e:
        session.rollback()  # Rollback in case of error
        click.echo(f"Error creating band: {e}")
    finally:
        session.close()  # Close the session

@cli.command()
@click.argument('title')
@click.argument('city')
def create_venue(title, city):
    """Create a new venue."""
    session = Session()  # Create a new session
    try:
        venue = Venue(title=title, city=city)
        session.add(venue)
        session.commit()
        click.echo(f"Venue '{title}' created successfully.")
    except Exception as e:
        session.rollback()
        click.echo(f"Error creating venue: {e}")
    finally:
        session.close()

@cli.command()
@click.argument('band_id')
@click.argument('venue_id')
@click.argument('date')
def create_concert(band_id, venue_id, date):
    """Create a new concert."""
    session = Session()  # Create a new session
    try:
        band = session.query(Band).get(band_id)
        venue = session.query(Venue).get(venue_id)
        if band and venue:
            concert = Concert(band=band, venue=venue, date=date)
            session.add(concert)
            session.commit()
            click.echo(f"Concert created successfully on {date}.")
        else:
            click.echo("Invalid band or venue ID.")
    except Exception as e:
        session.rollback()
        click.echo(f"Error creating concert: {e}")
    finally:
        session.close()

if __name__ == '__main__':
    cli()
