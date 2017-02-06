"""Models and database function for EXP Reviews"""

from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

################################################################################
# Model definitions

class User(db.Model):
    """User of EXP Reviews"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    email = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(64), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(5), nullable=False)


class Review(db.Model):
    """Reviews of games; contains score and comment"""

    __tablename__ = "reviews"

    review_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"),
                        nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey("games.game_id"),
                        nullable=False)
    score = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    review_time = db.Column(db.DateTime, nullable=False,
                            default=datetime.datetime.utcnow)

    user = db.relationship("User", backref="reviews")
    game = db.relationship("Game", backref="reviews")


class Game(db.Model):
    """Game data"""

    __tablename__ = "games"

    game_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    summary = db.Column(db.Text)
    storyline = db.Column(db.Text)
    release_date = db.Column(db.DateTime, nullable=False)
    cover_id = db.Column(db.Integer, db.ForeignKey("covers.cover_id"))
    collection_id = db.Column(db.Integer, db.ForeignKey("collections.collection_id"))
    franchise_id = db.Column(db.Integer, db.ForeignKey("franchise.franchise_id"))

    cover = db.relationship("Cover", backref="game")
    collection = db.relationship("Collection", backref="games")
    franchise = db.relationship("Franchise", backref="games")


class Cover(db.Model):
    """Game cover art image and dimensions"""

    __tablename__ = "covers"

    cover_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    url = db.Column(db.String(64), nullable=False)
    width = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)


class Collection(db.Model):
    """Collection data"""

    __tablename__ = "collections"

    collection_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64), nullable=False)


class Franchise(db.Model):
    """Franchise data"""

    __tablename__ = "franchises"

    franchise_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64), nullable=False)


class GameGenre(db.Model):
    """Association table between games and genres"""

    __tablename__ = "game_genres"

    gamegenre_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey("games.game_id"), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.genre_id"), nullable=False)


class Genre(db.Model):
    """Genre table"""

    __tablename__ = "genres"

    genre_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    genre = db.Column(db.String(32), nullable=False)

    games = db.relationship("Game", secondary="game_genres", backref="genres")


class GameDeveloper(db.Model):
    """Association table between games and developers"""

    __tablename__ = "game_developers"

    gamedev_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey("games.game_id"), nullable=False)
    developer_id = db.Column(db.Integer, db.ForeignKey("developers.developer_id"),
                             nullable=False)


class Developer(db.Model):
    """Developer table"""

    __tablename__ = "developers"

    developer_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

    games = db.relationship("Game", secondary="game_developers", backref="developers")


class GamePublisher(db.Model):
    """Association table between games and publishers"""

    __tablename__ = "game_publishers"

    gamepub_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey("games.game_id"), nullable=False)
    publisher_id = db.Column(db.Integer, db.ForeignKey("publishers.publisher_id"),
                             nullable=False)


class Publisher(db.Model):
    """Publisher table"""

    __tablename__ = "publishers"

    publisher_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

    games = db.relationship("Game", secondary="game_publishers", backref="publishers")


class GameVideo(db.Model):
    """Association table bwteen games and videos"""

    __tablename__ = "game_videos"

    gamevideo_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey("games.game_id"), nullable=False)
    video_id = db.Column(db.Integer, db.ForeignKey("videos.vieo_id"), nullable=False)


class Video(db.Model):
    """Video table"""

    __tablename__ = "videos"

    video_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    url = db.Column(db.String(64), nullable=False)

    game = db.relationship("Game", secondary="game_videos", backref="videos")


class GamePlatform(db.Model):
    """Association table between games and platforms"""

    __tablename__ = "game_platforms"

    gameplatform_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey("games.game_id"), nullable=False)
    platform_id = db.Column(db.Integer, db.ForeignKey("platforms.platform_id"),
                            nullable=False)


class Platform(db.Model):
    """Game platform table"""

    __tablename__ = "platforms"

    platform_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64), nullable=False)

    games = db.relationship("Game", secondary="game_videos", backref="platforms")




