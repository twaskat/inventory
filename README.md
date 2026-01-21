# Simple Inventory App

A minimal Flask application to track inventory items with persistent file storage. Perfect for listing items you've purchased or managing simple inventories.

## Features

- ✅ Add items to inventory
- ✅ List all items
- ✅ Persistent file storage
- ✅ RESTful API
- ✅ Ready for Railway deployment

## Local Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the app:
```bash
python app.py
```

3. Test the API:
```bash
# Get usage info
curl http://localhost:5000/

# Add an item
curl -X POST http://localhost:5000/inventory \
  -H "Content-Type: application/json" \
  -d '{"item": "Laptop"}'

# List all items
curl http://localhost:5000/inventory

# Clear inventory
curl -X DELETE http://localhost:5000/inventory
```

## API Endpoints

### `GET /`
Returns API usage information.

### `GET /inventory`
Returns all items in inventory.

**Response:**
```json
{
  "count": 2,
  "items": [
    {"item": "Laptop", "timestamp": "..."},
    {"item": "Mouse", "timestamp": "..."}
  ]
}
```

### `POST /inventory`
Add a new item to inventory.

**Request:**
```json
{
  "item": "Keyboard"
}
```

**Response:**
```json
{
  "message": "Item added successfully",
  "item": "Keyboard",
  "total_items": 3
}
```

### `DELETE /inventory`
Clear all items from inventory.

**Response:**
```json
{
  "message": "Inventory cleared successfully"
}
```

## Deploy to Railway

### Method 1: GitHub Integration (Recommended)

1. **Push your code to GitHub:**
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/inventory-app.git
git push -u origin main
```

2. **Deploy on Railway:**
   - Go to [railway.app](https://railway.app)
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway will automatically detect it's a Python app
   - Click "Deploy"

3. **Get your app URL:**
   - Railway will provide a URL like `https://your-app.railway.app`
   - Test it: `curl https://your-app.railway.app/inventory`

### Method 2: Railway CLI

1. **Install Railway CLI:**
```bash
npm install -g @railway/cli
```

2. **Login and deploy:**
```bash
railway login
railway init
railway up
```

### Method 3: Direct Import

1. Go to [railway.app](https://railway.app)
2. Click "New Project" → "Deploy from GitHub"
3. Select "Start from Scratch" or "Import from URL"

## Important Notes for Railway

- **Persistence**: Railway's file system is ephemeral. For true persistence in production, you would need to add a database (PostgreSQL, Redis, etc.). For this simple demo, data will persist between requests but may be reset on deployments/restarts.
- **Environment Variables**: The app automatically uses the PORT environment variable provided by Railway.
- **Logging**: Railway captures stdout/stderr, so you'll see Flask logs in the Railway dashboard.

## File Structure

```
.
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Procfile           # Railway process configuration
├── runtime.txt        # Python version specification
├── README.md          # This file
└── inventory.json     # Auto-generated inventory storage
```

## Customization

To add true persistence with a database:

1. Install PostgreSQL:
```bash
pip install psycopg2-binary
```

2. Modify `app.py` to use SQLAlchemy with PostgreSQL connection string from Railway environment variables.

## License

MIT License - feel free to use this for your projects!