from leads.models import Lead
from rest_framework import viewsets, permissions
from .serilizers import LeadSerilizer

# Lead Viewset
class LeadViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]    
    serializer_class = LeadSerilizer

    def get_queryset(self):
        return self.request.user.leads.all()
    
    def perform_create(self):
        serializer.save(owner = self.request.user)