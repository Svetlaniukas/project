// The updatePrice function in JavaScript is crafted to dynamically calculate and display the total price of a product,
// tailored to user-selected specifications. It starts by ensuring the base price is in a numerical format,
// accommodating the possibility of it being passed as a string. The function then proceeds to fetch additional costs
// associated with each product option—size, material, roof, and color—selected by the user.
// These costs are retrieved from the data attributes of selected options in their respective dropdown menus.
// After converting these values to integers for accurate calculation, the function sums them up with the base
// price to determine the total cost. This total is then promptly displayed in a designated area on the webpage,
// effectively keeping the user informed about the price impact of their selections in real-time.
// This approach enhances user interaction, providing a clear and immediate understanding of the cost 
//implications of different combinations of product features.

function updatePrice(basePrice) {
    
    basePrice = parseInt(basePrice);

    var sizePrice = document.getElementById('sizeSelect').selectedOptions[0].getAttribute('data-price');
    var materialPrice = document.getElementById('materialSelect').selectedOptions[0].getAttribute('data-price');
    var roofPrice = document.getElementById('roofSelect').selectedOptions[0].getAttribute('data-price');
    var colorPrice = document.getElementById('colorSelect').selectedOptions[0].getAttribute('data-price');

   
    var totalPrice = basePrice + parseInt(sizePrice) + parseInt(materialPrice) + parseInt(roofPrice) + parseInt(colorPrice);

    
    document.getElementById('totalPrice').innerHTML = 'Price: ' + totalPrice;
}
