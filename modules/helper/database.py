# @todo: What do we gain by not using everything directly?
# Is this legacy? When should the db be setup? Will it be helpful to create
# helper methods for myself?

# We need the app object since it contains the config data.
from helper.app import get_app
# Required by some of the models for database access.
from flaskext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm.properties import ColumnProperty
from sqlalchemy.sql.expression import func, and_

def check_if_entity_exists(entity):
    from helper.db import db

    entity_unique_constraints = entity.get_constraints_by_type(db.UniqueConstraint)
    # Check to see whether the values inside this list of columns already exists in the database
    # using a where key1 = agent.key1 and key2 = agent.key2 and key3 = agent.key3
    # Use getattr() to help build:
    # http://stackoverflow.com/questions/7604967/sqlalchemy-build-query-filter-dynamically-from-dict
    for constraint_columns in entity_unique_constraints:
        filter_clauses = []
        for constraint_column_name in constraint_columns:
            filter_clauses.append(
                getattr(entity.__class__, constraint_column_name) == getattr(entity, constraint_column_name))

        query = db.session.query(entity.__class__).filter(and_(*filter_clauses))
        # http://stackoverflow.com/questions/7092396/react-on-uniquekeyviolation-in-sqlalchemy
        from sqlalchemy.orm.exc import NoResultFound

        try:
            return query.one()
        except NoResultFound:
            pass
    return None


class LowerCaseComparator(ColumnProperty.Comparator):
    def __eq__(self, other):
        return func.lower(self.__clause_element__()) == func.lower(other)


class ConstraintsMixin(object):
    '''
    This class will never be used on its own. It will always be used with SQLAlchemy declarative_base classes
    to add extra functionality relating to fetching columns that are part of a particular type of constraint.
    '''

    def get_constraints_by_type(self, ConstraintClass=None):
        constraint_columns = []
        for constraint in self.__table__.constraints:
            if ConstraintClass is None or isinstance(constraint, ConstraintClass):
                constraint_columns.append([column.name for column in constraint.columns])
        return constraint_columns

app = get_app()
db = SQLAlchemy(app)
