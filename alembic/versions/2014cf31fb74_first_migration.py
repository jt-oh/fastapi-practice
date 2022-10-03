"""first migration

Revision ID: 2014cf31fb74
Revises: 
Create Date: 2022-10-03 16:23:38.609198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2014cf31fb74'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'my_users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(100), unique=True, index=True),
        sa.Column('hashed_password', sa.String(500)),
        sa.Column('age', sa.Integer),
        sa.Column('is_active', sa.Boolean, default=True),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime)
    )

    op.create_table(
        'my_items',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(100), index=True),
        sa.Column('description', sa.String(1000), index=True),
        sa.Column('owner_id', sa.Integer, sa.ForeignKey("my_users.id")),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime)
    )

    pass


def downgrade() -> None:
    op.drop_table('my_users')
    op.drop_table('my_items')

    pass
