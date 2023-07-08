"""customer

Revision ID: a5ff1a1232f8
Revises: fc955ab74891
Create Date: 2023-07-08 10:29:45.708715

"""
from alembic import op
import sqlalchemy as sa

from src.domain.v1.customer.model import CustomerModel

# revision identifiers, used by Alembic.
revision = 'a5ff1a1232f8'
down_revision = 'fc955ab74891'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        CustomerModel.__tablename__,
        sa.Column("customer_id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(255), nullable=True),
        sa.Column("image_url", sa.String(500), nullable=True),
        sa.Column("document", sa.String(11), nullable=True),
        sa.Column("cnpj", sa.String(14), nullable=True),
        sa.Column("active", sa.Boolean, default=True, nullable=True),
        sa.Column("email", sa.String(255), nullable=False),
        sa.Column("phone", sa.String(20), nullable=False),
        sa.Column("created_date", sa.DateTime, nullable=True),
        sa.Column("updated_date", sa.DateTime, nullable=True),
        sa.Column("user_id", sa.Integer, nullable=False)
    )

    op.create_foreign_key(
        'fk_customers_users',
        'customers', 'users',
        ['user_id'], ['user_id']
    )


def downgrade() -> None:
    op.drop_constraint('fk_customers_users', 'customers', type_='foreignkey')
    op.drop_table(CustomerModel.__tablename__)
