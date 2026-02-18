function formatPrice(value) {
    return "Rs. " + Number(value).toFixed(2);
}

$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    autoplay: true,
    responsive: {
        0: { items: 2, nav: false },
        600: { items: 4, nav: true },
        1000: { items: 6, nav: true, loop: true }
    }
});


/* =========================
   PLUS CART
========================= */
$(document).on('click', '.plus-cart', function () {
    let id = $(this).data("pid");     
    if (!id) return;
    let qtyElem = this.parentNode.children[2]; // SAME STYLE
    $.ajax({
        type: "GET",
        url: "/pluscart/",              
        data: { prod_id: id },
        success: function (data) {
            qtyElem.innerText = data.quantity;
            document.getElementById("amount").textContent = formatPrice(data.amount);
            document.getElementById("totalamount").textContent = formatPrice(data.totalamount);
        }
    });
});


/* =========================
   MINUS CART
========================= */
$(document).on('click', '.minus-cart', function () {
    let id = $(this).data("pid");
    if (!id) return;
    let qtyElem = this.parentNode.children[2];
    $.ajax({
        type: "GET",
        url: "/minuscart/",
        data: { prod_id: id },
        success: function (data) {
            qtyElem.innerText = data.quantity;
            document.getElementById("amount").textContent = formatPrice(data.amount);
            document.getElementById("totalamount").textContent = formatPrice(data.totalamount);
        }
    });
});


/* =========================
   REMOVE CART
========================= */
$(document).on('click', '.remove-cart', function () {
    let id = $(this).data("pid");
    if (!id) return;
    let element = this;
    $.ajax({
        type: "GET",
        url: "/removecart/",
        data: { prod_id: id },
        success: function (data) {
            document.getElementById("amount").textContent = formatPrice(data.amount);
            document.getElementById("totalamount").textContent = formatPrice(data.totalamount);
            element.closest(".row").remove();
        }
    });
});


/* =========================
   ADD TO WISHLIST
========================= */
$(document).on('click', '.plus-wishlist', function () {
    let id = $(this).data("pid");
    if (!id) return;
    $.ajax({
        type: "GET",
        url: "/pluswishlist/",
        data: { prod_id: id },
        success: function () {
            window.location.href = `/product-detail/${id}`;
        }
    });
});


/* =========================
   REMOVE FROM WISHLIST
========================= */
$(document).on('click', '.minus-wishlist', function () {
    let id = $(this).data("pid");
    if (!id) return;
    $.ajax({
        type: "GET",
        url: "/minuswishlist/",
        data: { prod_id: id },
        success: function () {
            window.location.href = `/product-detail/${id}`;
        }
    });
});

$('.plus-wishlist').click(function () {
    var id = $(this).attr("pid").toString();

    $.ajax({
        type: "GET",
        url: "/pluswishlist",
        data: {
            prod_id: id
        },
        success: function (data) {
            // alert(data.message)
            window.location.href = `http://localhost:8000/product-detail/${id}`;
        }
    });
});

$('.minus-wishlist').click(function () {
    var id = $(this).attr("pid").toString();

    $.ajax({
        type: "GET",
        url: "/minuswishlist",
        data: {
            prod_id: id
        },
        success: function (data) {
            window.location.href = `http://localhost:8000/product-detail/${id}`;
        }
    });
});
