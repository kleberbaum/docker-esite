import graphene

import esite.aqms.schema
import esite.home.schema


class Query(esite.home.schema.Query, esite.aqms.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query)
