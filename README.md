# Instrumentarium

**Instrumentarium** is a web application for selling and buying used musical instruments. It provides a platform for users to create accounts, list their instruments for sale, message other users and browse ads posted by others. The application also includes features for liking ads, receiving notifications for price changes, and an approval process for ads before they're visible to the public.

---

## Current Features

### Models
- **Ads Model**: Represents the advertisements for musical instruments.
- **Message and Chat Models**: Needed for the user's chat functionality.
- **User and Profile Models**: One-to-one relationship to manage user profiles and accounts.

### Functionalities
- **User Authentication**:
  - Register new users.
  - Log in and log out functionality.
  
- **Ad Management**:
  - Users can upload ads.
  - Admin approval required for each ad before it's visible on the site.

- **User Management**:
  - Users can update their profile information.

- **User Interaction with Ads**:
  - Users can **like** ads they are interested in.
  - Users receive **notifications** when the price or status of liked ads changes.

- **Messaging system**:
  - Users can text each other about ads.

---

## Planned Improvements

- **Search and Filter Ads**: Allow users to search for specific ads by criteria such as instrument type, price, etc.
- **Enhanced User Profiles**: Add additional fields for user profiles (e.g., contact information).
- **Notifications**: Notify users when the price or status of an ad changes, especially for ads they have liked.
- **Admin Dashboard**: Provide an admin interface to manage ads and approve or reject submissions.
