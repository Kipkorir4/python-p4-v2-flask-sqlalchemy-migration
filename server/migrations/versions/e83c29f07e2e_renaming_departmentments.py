"""renaming Departmentments

Revision ID: e83c29f07e2e
Revises: a2163f18a105
Create Date: 2024-06-26 15:27:45.731050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e83c29f07e2e'
down_revision = 'a2163f18a105'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
