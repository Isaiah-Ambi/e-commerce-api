# E-COMMERCE API

Sample solution for the [E-commerce API](https://roadmap.sh/projects/ecommerce-api) challenge from [roadmap.sh](https://roadmap.sh/).

## Features

- **User Authentication**: JWT-based signup, login, and profile management.
- **Product Management**: View, search, and detail endpoints for products.
- **Cart Management**: Add, remove, and view products in user carts.
- **Checkout**: Stripe integration for payments.
- **Protected Endpoints**: Cart and checkout actions require authentication.

## Tech Stack

- Django 5.2
- Django Ninja & Ninja JWT
- SQLite (default, easily swappable)
- Stripe (for payments)

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Isaiah-Ambi/e-commerce-api.git
   cd e-commerce\ api
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   - Create a `.env` file in the root directory:
     ```
     API_KEY=your_stripe_api_key
     ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication

- `POST /api/auth/token/` – Obtain JWT token
- `POST /api/auth/token/refresh/` – Refresh JWT token

### Products

- `GET /api/products/` – List all products
- `GET /api/products/search/{query}` – Search products by name

### Cart

- `GET /api/cart/` – View cart (JWT required)
- `GET /api/cart/add/{id}` – Add product to cart (JWT required)
- `DELETE /api/cart/remove/{id}` – Remove product from cart (JWT required)

### Checkout

- `POST /cart/checkout/` – Stripe payment integration (JWT required)

## Folder Structure

- `store_api/` – Django project settings and API root
- `products/` – Product models, API, and views
- `cart/` – Cart models, API, and views
- `users/` – User registration, login, and profile

## Testing

Run all tests:
```bash
python manage.py test
```

## License

MIT

---

*For more details, see the source code


