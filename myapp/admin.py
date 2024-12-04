from django.contrib import admin
from .models import Part, Product, Aircraft, Team, TeamPart, AircraftPart, ProductPart


# Admin panelleri için yapılandırmalar
@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity_in_stock')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')


@admin.register(Aircraft)
class AircraftAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(TeamPart)
class TeamPartAdmin(admin.ModelAdmin):
    list_display = ('id', 'team', 'part')


@admin.register(AircraftPart)
class AircraftPartAdmin(admin.ModelAdmin):
    list_display = ('id', 'aircraft', 'part', 'quantity_used')


@admin.register(ProductPart)
class ProductPartAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'part', 'quantity_used')


@admin.action(description="Seçilen parçalarla uçak üret")
def create_aircraft(modeladmin, request, queryset):
    for aircraft in queryset:
        # Gerekli parçaların kontrolü
        required_parts = {
            "kanat": 1,
            "gövde": 1,
            "kuyruk": 1,
            "aviyonik": 1,
        }
        missing_parts = []
        for part_name, quantity in required_parts.items():
            try:
                part = Part.objects.get(name=part_name)
                if part.quantity_in_stock < quantity:
                    missing_parts.append(part_name)
                else:
                    part.quantity_in_stock -= quantity
                    part.save()
            except Part.DoesNotExist:
                missing_parts.append(part_name)

        # Eksik parça varsa hata mesajı
        if missing_parts:
            modeladmin.message_user(
                request,
                f"{aircraft.name} için eksik parçalar: {', '.join(missing_parts)}",
                level="error"
            )
            continue

        # Uçak üretimi
        aircraft.is_completed = True
        aircraft.save()
        modeladmin.message_user(request, f"{aircraft.name} başarıyla üretildi!", level="success")

