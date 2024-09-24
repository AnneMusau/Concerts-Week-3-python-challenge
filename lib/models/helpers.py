from system import Band, Venue, Concert

def find_band_by_name(session, name):
    """Find a band by its name."""
    band = session.query(Band).filter_by(name=name).first()
    return band

def find_venue_by_title(session, title):
    """Find a venue by its title."""
    venue = session.query(Venue).filter_by(title=title).first()
    return venue

def find_concert(session, band_name, venue_title, date):
    """Find a concert by band name, venue title, and date."""
    concert = session.query(Concert).filter_by(date=date).first()
    if concert and concert.band.name == band_name and concert.venue.title == venue_title:
        return concert
    return None

def list_all_bands(session):
    """List all bands in the database."""
    return session.query(Band).all()

def list_all_venues(session):
    """List all venues in the database."""
    return session.query(Venue).all()

def list_all_concerts(session):
    """List all concerts in the database."""
    return session.query(Concert).all()