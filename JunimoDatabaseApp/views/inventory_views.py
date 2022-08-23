# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.exceptions import PermissionDenied
# from rest_framework import generics, status
# from django.shortcuts import get_object_or_404

# from JunimoDatabaseApp.models import character

# from ..models.character import Character
# from ..models.inventory import Inventory
# from ..serializers import CharacterSerializer
# from ..serializers import InventorySerializer

# # 

# # Create your views here.
# class Inventories(generics.ListCreateAPIView):
#     permission_classes=(IsAuthenticated,)
#     serializer_class = InventorySerializer
#     def get(self, request):
#         """Index request"""
#         # Get all the characters' inventories:
#         characters = Character.objects.all()
#         inventories = Inventory.objects.all()
#         # Filter the characters by owner, so you can only see your owned characters
#         characters = Character.objects.filter(owner=request.user.id)
#         # Filter the inventories by character, so you can only see your owned inventories
#         inventories = Inventory.objects.filter(character_id=characters)
#         # Run the data through the serializer
#         data = InventorySerializer(characters, many=True).data
#         return Response({ 'inventories': data })

#     def post(self, request):
#         """Create request"""
#         # Add user to request data object
#         request.data['character']['owner'] = request.user.id
#         # Serialize/create mango
#         mango = CharacterSerializer(data=request.data['character'])
#         # If the mango data is valid according to our serializer...
#         if character.is_valid():
#             # Save the created mango & send a response
#             character.save()
#             return Response({ 'character': character.data }, status=status.HTTP_201_CREATED)
#         # If the data is not valid, return a response with the errors
#         return Response(character.errors, status=status.HTTP_400_BAD_REQUEST)

# class CharacterDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes=(IsAuthenticated,)
#     def get(self, request, pk):
#         """Show request"""
#         # Locate the mango to show
#         character = get_object_or_404(Character, pk=pk)
#         # Only want to show owned characters?
#         if request.user != character.owner:
#             raise PermissionDenied('Unauthorized, you do not own this character')

#         # Run the data through the serializer so it's formatted
#         data = CharacterSerializer(character).data
#         return Response({ 'character': data })

#     def delete(self, request, pk):
#         """Delete request"""
#         # Locate mango to delete
#         character = get_object_or_404(Character, pk=pk)
#         # Check the characters's owner against the user making this request
#         if request.user != character.owner:
#             raise PermissionDenied('Unauthorized, you do not own this character')
#         # Only delete if the user owns the character
#         character.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     def partial_update(self, request, pk):
#         """Update Request"""
#         # Locate Character
#         # get_object_or_404 returns a object representation of our Character
#         character = get_object_or_404(Character, pk=pk)
#         # Check the character's owner against the user making this request
#         if request.user != character.owner:
#             raise PermissionDenied('Unauthorized, you do not own this character')

#         # Ensure the owner field is set to the current user's ID
#         request.data['character']['owner'] = request.user.id
#         # Validate updates with serializer
#         data = CharacterSerializer(character, data=request.data['character'], partial=True)
#         if data.is_valid():
#             # Save & send a 204 no content
#             data.save()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         # If the data is not valid, return a response with the errors
#         return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)