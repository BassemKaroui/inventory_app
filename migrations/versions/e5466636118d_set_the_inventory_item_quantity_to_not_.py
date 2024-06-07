"""set the inventory_item.quantity to not nullable, with a default value of 0

Revision ID: e5466636118d
Revises: fa9f52c0b269
Create Date: 2024-05-10 12:01:22.041351

"""

from http import server
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "e5466636118d"
down_revision: Union[str, None] = "fa9f52c0b269"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "inventory_item",
        "quantity",
        existing_type=sa.INTEGER(),
        server_default="0",
        nullable=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "inventory_item", "quantity", existing_type=sa.INTEGER(), nullable=True
    )
    # ### end Alembic commands ###
