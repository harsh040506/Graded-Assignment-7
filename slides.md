---
marp: true
title: Product Documentation Presentation
# This fulfills the email requirement
author: 24f3004403@ds.study.iitm.ac.in
# This fulfills the page numbers requirement
paginate: true
theme: gaia
---

<!-- This <style> block fulfills the custom theme specification requirement -->
<style>
  h1, h2 {
    color: #005f99; /* A professional blue color for headers */
  }
  section {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
  .lead-slide {
    text-align: center;
    padding: 40px;
    justify-content: center;
  }
</style>

<!-- 
  This is the Title Slide.
  The "_class" directive applies our custom CSS class. 
-->
<!-- _class: lead-slide -->

# Our New Product API
### A Guide for Developers
**By: 24f3004403@ds.study.iitm.ac.in**

---

## Agenda

1.  Introduction & Core Concepts
2.  Key Features & Endpoints
3.  Performance & Complexity
4.  Q&A

---

<!-- 
  This slide fulfills the background image requirement.
  It uses a relative path to the image you saved in Step 3.
-->

![bg fit](images/background.jpg)

## Key Features Overview

- **Scalability**: Built to handle millions of requests.
- **Security**: OAuth 2.0 and End-to-End Encryption.
- **Flexibility**: RESTful endpoints for easy integration.

---

<!-- 
  This slide fulfills the custom styling with directives requirement.
  It sets a custom background and text color just for this slide.
-->
<!-- _backgroundColor: #282c34 -->
<!-- _color: #ffffff -->

## Code Samples

Here is how you make a simple API call:

```python
import requests

def get_user_data(api_key, user_id):
    url = f"https://api.ourproduct.com/v1/users/{user_id}"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)
    return response.json()