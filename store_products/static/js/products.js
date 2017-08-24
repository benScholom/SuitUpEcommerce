$(document).ready(function() {

var cart = []
//use buy button to get id and add the number to the cart
$('.buy').on("click", function() {
	id = $(this).attr('id');
	addToCart(id);
});
//display items in cart
function showCart() {
	if(localStorage.getItem("cart") !== null) {
		cart = JSON.parse(localStorage.cart);
		console.log(cart);
	} else {
		cart = [];
	}
	//use id in local storage to create and populate necessary elements
var cartElem = $("#cart");
cartElem.html("");
for(var i = 0; i < cart.length; i++){
	var item = cart[i];
	console.log(item);
	var product =$('<li />').attr('id', "li"+item);
	product.appendTo(cartElem);
	var spitem = $('<span />').addClass('item');
	spitem.appendTo(product);
	var spitemleft = $('<span />').addClass('item-left');
	spitemleft.appendTo(spitem);
	img_url = $('#img'+ item).attr('src');
	var img = $("<img />").attr('src', img_url)
	img.appendTo(spitemleft);
	var spitemcenter = $('<span />').addClass('item-info');
	spitemcenter.appendTo(spitemleft);
	var title = $('#name'+item).text();
	var name = $('<span />').addClass('name').text(title);
	name.appendTo(spitemcenter);
	var number = $('#price'+item).text();
	var price = $('<span />').addClass('price').text(number);
	price.appendTo(spitemcenter);
	var spitemright = $('<span />').addClass('item-right');
	spitemright.appendTo(spitem)
	var deletebtn = $('<button />').addClass("btn btn-xs btn-danger pull-right").data('item', item).text('x');
	deletebtn.appendTo(spitemright);
}
cartElem.append('<li class="text-center"><button class="btn-default" id="checkout">Checkout</button></li>');
}
//clear cart
function clear() {
	localStorage.clear();
	showCart();
}
//add item to cart in localstorage
function addToCart(product) {
	cart.push(product);
	localStorage.setItem('cart', JSON.stringify(cart));
	showCart();
}

//event listener for delete buttons
$('.btn-danger').on('click', function() {
	console.log('hey');
	var select = $(this).data('item');
	console.log(select);
	var index = cart.indexOf(select);
	if (index > -1) {
    cart = cart.splice(index, 1);
    localStorage.removeItem('cart');
	$('#li'+select).remove();
	localStorage.setItem('cart', JSON.stringify(cart));
}

});

});
