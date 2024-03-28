import React from 'react';

const ProductDetail = ({ product }) => {
    // Implementation for displaying detailed information about a specific product
    return (
        <div>
            <h2>Product Detail</h2>
            <p>Name: {product.name}</p>
            <p>Description: {product.description}</p>
            <p>Price: ${product.price}</p>
        </div>
    );
}

export default ProductDetail;