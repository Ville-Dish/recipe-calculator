# Recipe Calculator

A modern, responsive web app for scaling recipes to any size, with support for metric and imperial units. Built with [Tailwind CSS 4](https://tailwindcss.com/) and vanilla JavaScript.  
**Perfect for home cooks, bakers, and anyone who wants to scale recipes up or down!**

## ✨ Features

- **Mobile Responsive**: Looks great on all devices
- **Smart Scaling**: Scale any recipe by any base ingredient and amount
- **Multiple Units**: Supports g, kg, oz, lb, ml, l, tsp, tbsp, cups, qt, and more
- **Unit Conversion**: Switch between metric, imperial, or mixed units
- **Extensible**: Easily add new recipes in `script.js`
- **Modern UI**: Clean, intuitive interface with Tailwind CSS 4

## 🚀 Live Demo

> _Host your app on GitHub Pages and put the link here!_

## 📦 Files

- `index.html` – Main HTML file
- `script.js` – All app logic and recipe data
- `README.md` – This documentation

## 🛠️ How to Use

1. **Clone or download** this repository.
2. Open `index.html` in your browser, or [deploy to GitHub Pages](#-deployment-to-github-pages).
3. **Select a recipe** from the dropdown.
4. **Choose a base ingredient** (e.g., flour).
5. **Enter the desired amount** and select the unit.
6. Click **Calculate Recipe**.
7. View the **scaled recipe** in your preferred units (metric, imperial, or mixed).

## 🧑‍🍳 Example: Milk Chinchin

- **Original**: 1.5 kg flour, 200g butter, 2.5 cups sugar, etc.
- **Want to make with 3kg flour?**  
  - Select "flour" as base ingredient, enter "3", select "kg", and calculate.
  - All other ingredients are scaled up automatically.

## ➕ Adding New Recipes

Edit the `recipes` object in `script.js`.  
Example:

```js
const recipes = {
  'milk-chinchin': {
    name: 'Milk Chinchin',
    baseIngredient: 'flour',
    ingredients: {
      flour: { amount: 1.5, unit: 'kg', type: 'weight' },
      butter: { amount: 200, unit: 'g', type: 'weight' },
      // ... more ingredients
    }
  },
  'my-new-recipe': {
    name: 'My New Recipe',
    baseIngredient: 'sugar',
    ingredients: {
      sugar: { amount: 500, unit: 'g', type: 'weight' },
      water: { amount: 1, unit: 'l', type: 'volume' },
      // ... more ingredients
    }
  }
};
```

- **unit**: Use `g`, `kg`, `oz`, `lb` for weight; `ml`, `l`, `tsp`, `tbsp`, `cups`, `qt` for volume; or `eggs` for count.
- **type**: `"weight"`, `"volume"`, or `"count"`.

## 📏 Supported Units

**Weight:**  
- Grams (`g`), Kilograms (`kg`), Ounces (`oz`), Pounds (`lb`)

**Volume:**  
- Milliliters (`ml`), Liters (`l`), Teaspoons (`tsp`), Tablespoons (`tbsp`), Cups (`cups`), Quarts (`qt`)

**Count:**  
- Eggs, etc.

## 🌐 Deployment to GitHub Pages

1. **Create a new GitHub repository** and upload `index.html`, `script.js`, and `README.md`.
2. Go to **Settings → Pages**.
3. Under "Source", select your branch (usually `main`) and `/ (root)` folder.
4. Save.  
   Your app will be live at:  
   `https://yourusername.github.io/repository-name`

## 🖼️ Screenshots

_Add screenshots here if you want!_

## 🛡️ License

MIT

---

**Enjoy your scalable, modern recipe calculator!**  
Questions or suggestions? [Open an issue](https://github.com/) or submit a PR!
