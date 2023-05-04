"""teste 1

Revision ID: 22f2e9043494
Revises: 
Create Date: 2023-05-03 23:18:20.818402

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa

from src.domain.v1.assists.models import AssistsModel
from src.domain.v1.cards.model import CardsModel
from src.domain.v1.goals.model import GoalsModel
from src.domain.v1.lineup_starts.model import LineUpStartsModel
from src.domain.v1.lineups.model import LineUpsModel
from src.domain.v1.matches.model import MatchesModel
from src.domain.v1.players.model import PlayersModel
from src.domain.v1.roles.model import RolesModel
from src.domain.v1.teams.model import TeamsModel
from src.domain.v1.tournaments.model import TournamentsModel
from src.domain.v1.users.model import UsersModel

# revision identifiers, used by Alembic.
revision = '22f2e9043494'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Roles
    op.create_table(
        RolesModel.__tablename__,
        sa.Column("role_id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(45), nullable=False)
    )
    """
    Ex de bulk 
    op.bulk_insert(
    account_table,
    [
        {"name": "A1", "description": "account 1"},
        {"name": "A2", "description": "account 2"},
    ],
)
    """

    # Tournaments
    op.create_table(
        TournamentsModel.__tablename__,
        sa.Column("tournament_id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(length=45)),
        sa.Column("image_url", sa.String(length=500)),
        sa.Column("active", sa.Boolean, default=True, nullable=False),
        sa.Column("created_date", sa.DateTime, default=datetime.now(), nullable=True),
        sa.Column("updated_date", sa.DateTime, default=datetime.now(), nullable=True)
    )

    # Teams
    op.create_table(
        TeamsModel.__tablename__,
        sa.Column("team_id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(length=45)),
        sa.Column("image_url", sa.String(length=500)),
        sa.Column("profile_desc", sa.Text),
        sa.Column("created_date", sa.DateTime, default=datetime.now(), nullable=True),
        sa.Column("updated_date", sa.DateTime, default=datetime.now(), nullable=True)
    )

    # Users
    op.create_table(
        UsersModel.__tablename__,
        sa.Column("user_id", sa.Integer, primary_key=True),
        sa.Column("role_id", sa.Integer, nullable=False),
        sa.Column("name", sa.String(length=60), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("phone", sa.String(length=15), nullable=False),
        sa.Column("password", sa.Text, nullable=False),
        sa.Column("status", sa.String(length=30)),
        sa.Column("active", sa.Boolean, default=True, nullable=False),
        sa.Column("created_date", sa.DateTime, default=datetime.now(), nullable=True),
        sa.Column("updated_date", sa.DateTime, default=datetime.now(), nullable=True)
    )

    # Players
    op.create_table(
        PlayersModel.__tablename__,
        sa.Column("player_id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, nullable=False),
        sa.Column("team_id", sa.Integer, nullable=True),
        sa.Column("goals_id", sa.Integer, nullable=True),
        sa.Column("nickname", sa.String(length=40)),
        sa.Column("status", sa.String(length=40)),
        sa.Column("image_url", sa.String(length=500)),
        sa.Column("profile_desc", sa.Text),
        sa.Column("main_position", sa.String(length=30)),
        sa.Column("secondary_position", sa.String(length=30)),
        sa.Column("signed", sa.Boolean, default=False),
        sa.Column("created_date", sa.DateTime, default=datetime.now(), nullable=True),
        sa.Column("updated_date", sa.DateTime, default=datetime.now(), nullable=True)
    )

    # Matches
    op.create_table(
        MatchesModel.__tablename__,
        sa.Column("match_id", sa.Integer, primary_key=True),
        sa.Column("team_home", sa.Integer, nullable=False),
        sa.Column("team_away", sa.Integer, nullable=False),
        sa.Column("tournaments", sa.Integer, nullable=True),
        sa.Column("created_date", sa.DateTime, default=datetime.now(), nullable=True),
        sa.Column("updated_date", sa.DateTime, default=datetime.now(), nullable=True)
    )

    # Assists
    op.create_table(
        AssistsModel.__tablename__,
        sa.Column("assist_id", sa.Integer, primary_key=True),
        sa.Column("match_id", sa.Integer, nullable=True),
        sa.Column("player_id", sa.Integer, nullable=False),
        sa.Column("created_date", sa.DateTime, default=datetime.now(), nullable=True),
        sa.Column("updated_date", sa.DateTime, default=datetime.now(), nullable=True)
    )

    # Cards
    op.create_table(
        CardsModel.__tablename__,
        sa.Column("card_id", sa.Integer, primary_key=True),
        sa.Column("match_id", sa.Integer, nullable=True),
        sa.Column("color", sa.String(length=1), nullable=False),
        sa.Column("created_date", sa.DateTime, default=datetime.now(), nullable=True),
        sa.Column("updated_date", sa.DateTime, default=datetime.now(), nullable=True),
    )

    # Goals
    op.create_table(
        GoalsModel.__tablename__,
        sa.Column("goal_id", sa.Integer, primary_key=True),
        sa.Column("match_id", sa.Integer, nullable=False),
        sa.Column("player_id", sa.Integer, nullable=False),
        sa.Column("created_date", sa.DateTime, default=datetime.now(), nullable=True),
    )

    # Lineups
    op.create_table(
        LineUpsModel.__tablename__,
        sa.Column("lineup_id", sa.Integer, primary_key=True),
        sa.Column("match_id", sa.Integer, nullable=False),
        sa.Column("formation", sa.String(length=10)),
        sa.Column("created_date", sa.DateTime, default=datetime.now(), nullable=True),
        sa.Column("updated_date", sa.DateTime, default=datetime.now(), nullable=True)
    )

    # Lineup Starts
    op.create_table(
        LineUpStartsModel.__tablename__,
        sa.Column("lineup_start_id", sa.Integer, primary_key=True),
        sa.Column("lineup_id", sa.Integer, nullable=False),
        sa.Column("player_id", sa.Integer, nullable=False),
        sa.Column("created_date", sa.DateTime, default=datetime.now(), nullable=True),
        sa.Column("updated_date", sa.DateTime, default=datetime.now(), nullable=True)
    )

    op.create_foreign_key(
        'fk_users_role',
        'users', 'roles',
        ['user_id'], ['role_id'],
    )


def downgrade() -> None:
    op.drop_table(UsersModel.__tablename__)  # has Roles FK
    op.drop_table(PlayersModel.__tablename__)
    op.drop_table(MatchesModel.__tablename__)
    op.drop_table(AssistsModel.__tablename__)
    op.drop_table(CardsModel.__tablename__)
    op.drop_table(GoalsModel.__tablename__)
    op.drop_table(LineUpsModel.__tablename__)
    op.drop_table(LineUpStartsModel.__tablename__)
    op.drop_table(RolesModel.__tablename__)
    op.drop_table(TeamsModel.__tablename__)
    op.drop_table(TournamentsModel.__tablename__)
