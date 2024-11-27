# Instrumentarium

**Instrumentarium** is a web application for selling and buying used musical instruments. It provides a platform for users to create accounts, list their instruments for sale, and browse ads posted by others. The application also includes features for liking ads, receiving notifications for price changes, and an approval process for ads before they're visible to the public.

---

## Current Features

### Models
- **Ads Model**: Represents the advertisements for musical instruments.
- **User and Account Models**: One-to-one relationship to manage user profiles and accounts.

### Functionalities
- **User Authentication**:
  - Register new users.
  - Log in and log out functionality.
  
- **Ad Management**:
  - Users can upload ads (ads are not yet associated with users).
  - Admin approval required for each ad before it's visible on the site.

- **User Interaction with Ads**:
  - Users can **like** ads they are interested in.
  - Users receive **notifications** when the price or status of liked ads changes.

---

## Planned Improvements

- **Ad Ownership**: Associate ads with user accounts.
- **Search and Filter Ads**: Allow users to search for specific ads by criteria such as instrument type, price, etc.
- **Enhanced User Profiles**: Add additional fields for user profiles (e.g., contact information).
- **Messaging System**: Implement a system for buyers and sellers to communicate directly through the platform.
- **Notifications**: Notify users when the price or status of an ad changes, especially for ads they have liked.
- **Admin Dashboard**: Provide an admin interface to manage ads and approve or reject submissions.
