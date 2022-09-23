"""
Root GraphQL Schema
"""
import graphene

import signals.schema


class Query(signals.schema.Query, graphene.ObjectType): # pylint: disable=too-few-public-methods
    """Abstract Query Class

    Args:
        signals (_type_): _description_
        graphene (_type_): _description_
    """
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project

schema = graphene.Schema(query=Query)
