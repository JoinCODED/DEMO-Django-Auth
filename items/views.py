from django.shortcuts import redirect, render

from items.forms import ItemForm
from .models import Item

# Create your views here.
def get_items(req):
    if req.user.is_anonymous:
        return redirect("signin")
    items = Item.objects.all()
    _items = []
    for item in items:
        _items.append(
            {
                "id": item.id,
                "name": item.name,
                "price": item.price,
                "image": item.image,
                "category": {
                    "name": f"Delicious {item.category.name}",
                    "image": item.category.image,
                }
            }
        )
    context = {"items": _items}
    return render(req, "item_list.html", context)

def get_item(req, item_id):
    item = Item.objects.get(id=item_id)
    comments = item.comments.all()
    _comments = []
    for comment in comments:
        _comments.append({"message": comment.message})
    context = {
               "item": { 
                    "id": item.id,
                    "name": item.name,
                    "price": item.price - 0.5,
                    "image": item.image,
                },
                "comments": _comments
            }
    print(context)
    return render(req, "item_detail.html", context)


def create_item(req):
    form = ItemForm()
    if req.method == "POST":
        form = ItemForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("item_list")
    context = {"form": form}
    return render(req, "item_create.html", context)