# Instrumentarium

**Instrumentarium** is a web application for selling and buying used musical instruments. It provides a platform for users to create accounts, list their instruments for sale and message other users. The application also includes features for liking ads and an approval process for ads before they're visible to the public.

---

## Current Features

### Models
- **Ad Model**: Represents the advertisements for musical instruments.
- **Like Model**: Represents the likes for advertisements.
- **Message and Chat Models**: Needed for the user's chat functionality.
- **User and Profile Models**: One-to-one relationship to manage user profiles and accounts.

### Functionalities
- **User Authentication**:
  - Register new users.
  - Log in and log out functionality.
  - Change password functionality.

- **Admin and Moderator dashboards**:
  - Users who have admin/moderator permissions have special dashboard to manage other user's ads and profiles.
  
- **Ad Management**:
  - Users can upload and update ads.
  - Admin approval required for each ad before it's visible on the site.
  - Moderators and Admins can activate/deactivate ads.

- **User Management**:
  - Users can update their profile information.

- **User Interaction with Ads**:
  - Users can **like** ads they are interested in.

- **Messaging system**:
  - Users can text each other about ads.

---

## Planned Improvements
- **Search and Filter Ads**: Allow users to search for specific ads by criteria such as instrument type, price, etc.
- **Notifications**: Notify users when the price or status of an ad changes, especially for ads they have liked.


## Installation
Follow these steps to set up the **Instrumentarium** project on your local machine:

### 1. Clone the repository
Clone this repository to your local machine using Git:

```bash
git clone https://github.com/Stoyan-Rusev/instrumentarium.git
cd instrumentarium
```

### 2. Set up a virtual environment
It's recommended to use a virtual environment to manage project dependencies:

#### For macOs/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
Once the virtual environment is activated, install the required dependencies using the requirements.txt file:

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a .env file in the root directory of your project to store sensitive information such as your secret key and database configuration.

### 5.Run database migrations
To set up the database schema, run the migrations:

```bash
python manage.py migrate
```

### 6. Create a superuser (optional)
If you'd like to create an admin user to access the Django admin panel, run the following command and follow the prompts:

```bash
python manage.py createsuperuser
```

### 7. Run the development server
Now, start the Django development server:

```bash
python manage.py runserver
```
