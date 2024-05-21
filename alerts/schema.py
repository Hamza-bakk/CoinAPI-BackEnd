import graphene
from graphene_django import DjangoObjectType
from .models import Alerts
from users.models import UserAccount
from datetime import datetime

class UserAccountType(DjangoObjectType):
    class Meta:
        model = UserAccount
        fields = ("id", "email", "first_name", "last_name")

class AlertsType(DjangoObjectType):
    class Meta:
        model = Alerts
        fields = ("id", "userId", "asset", "current_price", "target_price", "is_open", "open_date")

class Query(graphene.ObjectType):
    all_alerts = graphene.List(AlertsType)
    alert_by_id = graphene.Field(AlertsType, id=graphene.ID(required=True))
    alerts_by_user_id = graphene.List(AlertsType, user_id=graphene.ID(required=True))

    
    def resolve_all_alerts(root, info):
        return Alerts.objects.all()

    def resolve_alert_by_id(root, info, id):
        try:
            return Alerts.objects.get(pk=id)
        except Alerts.DoesNotExist:
            return None
    def resolve_alerts_by_user_id(root, info, user_id):
        return Alerts.objects.filter(userId=user_id)

class CreateAlerts(graphene.Mutation):
    class Arguments:
        userId = graphene.ID(required=True)
        asset = graphene.String(required=True)
        current_price = graphene.Int(required=True)
        target_price = graphene.Int(required=True)
        is_open = graphene.Boolean(required=True)
        open_date = graphene.DateTime(required=False)
        
    alerts = graphene.Field(AlertsType)
    
    def mutate(self, info, userId, asset, current_price, target_price, is_open, open_date=None):
        user = UserAccount.objects.get(pk=userId)
        if open_date is None:
            open_date = datetime.now()
        alerts = Alerts.objects.create(
            userId=user, 
            asset=asset, 
            current_price=current_price, 
            target_price=target_price, 
            is_open=is_open, 
            open_date=open_date
        )
        return CreateAlerts(alerts=alerts)

class UpdateAlerts(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        asset = graphene.String()
        target_price = graphene.Int()
        current_price = graphene.Int()
        is_open = graphene.Boolean()
        
    alerts = graphene.Field(AlertsType)
    
    def mutate(self, info, id, asset=None, current_price=None ,target_price=None, is_open=None):
        alerts = Alerts.objects.get(pk=id)
        if asset is not None:
            alerts.asset = asset
        if target_price is not None:
            alerts.target_price = target_price
        if is_open is not None:
            alerts.is_open = is_open
        if current_price is not None:
            alerts.current_price = current_price
        alerts.save()
        return UpdateAlerts(alerts=alerts)
    
class DeleteAlerts(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    alerts_id = graphene.ID()
    
    def mutate(self, info, id):
        alerts = Alerts.objects.get(pk=id)
        alerts.delete()
        return DeleteAlerts(alerts_id=id)
    
class Mutation(graphene.ObjectType):
    create_alerts = CreateAlerts.Field()
    update_alerts = UpdateAlerts.Field()
    delete_alerts = DeleteAlerts.Field()
    
schema = graphene.Schema(query=Query, mutation=Mutation)
