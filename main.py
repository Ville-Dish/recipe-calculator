import os

# Create the project structure
os.makedirs('recipe-calculator', exist_ok=True)
os.chdir('recipe-calculator')

# Create index.html
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recipe Calculator</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: {
                            50: '#fef7ee',
                            100: '#fdedd3',
                            500: '#f97316',
                            600: '#ea580c',
                            700: '#c2410c',
                        }
                    }
                }
            }
        }
    </script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</head>
<body class="bg-gray-50 min-h-screen">
    <!-- Header -->
    <header class="bg-white shadow-sm border-b">
        <div class="max-w-4xl mx-auto px-4 py-6">
            <h1 class="text-3xl font-bold text-gray-900 text-center">
                <i class="fas fa-calculator text-primary-500 mr-2"></i>
                Recipe Calculator
            </h1>
            <p class="text-gray-600 text-center mt-2">Scale your favorite recipes to any size</p>
        </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-4xl mx-auto px-4 py-8">
        <!-- Recipe Selection -->
        <div class="bg-white rounded-xl shadow-sm border p-6 mb-8">
            <h2 class="text-xl font-semibold text-gray-900 mb-4">
                <i class="fas fa-utensils text-primary-500 mr-2"></i>
                Select Recipe
            </h2>
            <select id="recipeSelect" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition-colors">
                <option value="">Choose a recipe...</option>
                <option value="milk-chinchin">Milk Chinchin</option>
            </select>
        </div>

        <!-- Recipe Details -->
        <div id="recipeDetails" class="hidden">
            <!-- Base Recipe Info -->
            <div class="bg-white rounded-xl shadow-sm border p-6 mb-8">
                <h3 class="text-xl font-semibold text-gray-900 mb-4">
                    <i class="fas fa-info-circle text-primary-500 mr-2"></i>
                    Base Recipe
                </h3>
                <div id="baseRecipe" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4"></div>
            </div>

            <!-- Calculator -->
            <div class="bg-white rounded-xl shadow-sm border p-6 mb-8">
                <h3 class="text-xl font-semibold text-gray-900 mb-4">
                    <i class="fas fa-balance-scale text-primary-500 mr-2"></i>
                    Scale Recipe
                </h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-2">
                            Select Base Ingredient
                        </label>
                        <select id="baseIngredient" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500">
                        </select>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-2">
                            Desired Amount
                        </label>
                        <div class="flex gap-2">
                            <input type="number" id="desiredAmount" placeholder="Enter amount" 
                                   class="flex-1 p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500" 
                                   step="0.01" min="0">
                            <select id="desiredUnit" class="p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500">
                            </select>
                        </div>
                    </div>
                </div>
                <button id="calculateBtn" class="w-full mt-6 bg-primary-500 hover:bg-primary-600 text-white font-semibold py-3 px-6 rounded-lg transition-colors">
                    <i class="fas fa-calculator mr-2"></i>
                    Calculate Recipe
                </button>
            </div>

            <!-- Results -->
            <div id="results" class="hidden bg-white rounded-xl shadow-sm border p-6">
                <h3 class="text-xl font-semibold text-gray-900 mb-4">
                    <i class="fas fa-list-check text-primary-500 mr-2"></i>
                    Scaled Recipe
                </h3>
                <div class="mb-4">
                    <label class="block text-sm font-medium text-gray-700 mb-2">Display Units</label>
                    <select id="displayUnit" class="p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500">
                        <option value="metric">Metric (g, kg, ml, l)</option>
                        <option value="imperial">Imperial (oz, lb, cups, tbsp, tsp)</option>
                        <option value="mixed">Mixed Units</option>
                    </select>
                </div>
                <div id="scaledRecipe" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4"></div>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-white border-t mt-16">
        <div class="max-w-4xl mx-auto px-4 py-6 text-center text-gray-600">
            <p>&copy; 2024 Recipe Calculator. Built with ❤️ for home cooks.</p>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>'''

with open('index.html', 'w') as f:
    f.write(html_content)

# Create script.js
js_content = '''// Recipe data structure
const recipes = {
    'milk-chinchin': {
        name: 'Milk Chinchin',
        baseIngredient: 'flour',
        ingredients: {
            flour: { amount: 1.5, unit: 'kg', type: 'weight' },
            butter: { amount: 200, unit: 'g', type: 'weight' },
            sugar: { amount: 2.5, unit: 'cups', type: 'volume' },
            bakingPowder: { amount: 7, unit: 'tsp', type: 'volume' },
            nutmeg: { amount: 6, unit: 'tsp', type: 'volume' },
            salt: { amount: 2.5, unit: 'tsp', type: 'volume' },
            eggs: { amount: 4, unit: 'eggs', type: 'count' },
            milk: { amount: 345, unit: 'ml', type: 'volume' },
            vanillaPowder: { amount: 1.5, unit: 'tsp', type: 'volume' },
            butterVanillaEmulsion: { amount: 1, unit: 'tsp', type: 'volume' },
            milkFlavor: { amount: 1, unit: 'tsp', type: 'volume' }
        }
    }
};

// Unit conversion factors (to grams for weight, to ml for volume)
const conversions = {
    weight: {
        g: 1,
        kg: 1000,
        oz: 28.35,
        lb: 453.59
    },
    volume: {
        ml: 1,
        l: 1000,
        tsp: 4.93,
        tbsp: 14.79,
        cups: 236.59,
        qt: 946.35,
        'fl oz': 29.57
    }
};

// Display units for different systems
const displayUnits = {
    metric: {
        weight: { small: 'g', large: 'kg', threshold: 1000 },
        volume: { small: 'ml', large: 'l', threshold: 1000 }
    },
    imperial: {
        weight: { small: 'oz', large: 'lb', threshold: 16 },
        volume: { small: 'tsp', medium: 'tbsp', large: 'cups', thresholds: [3, 16] }
    }
};

// Current recipe and scale factor
let currentRecipe = null;
let scaleFactor = 1;

// DOM elements
const recipeSelect = document.getElementById('recipeSelect');
const recipeDetails = document.getElementById('recipeDetails');
const baseRecipe = document.getElementById('baseRecipe');
const baseIngredient = document.getElementById('baseIngredient');
const desiredAmount = document.getElementById('desiredAmount');
const desiredUnit = document.getElementById('desiredUnit');
const calculateBtn = document.getElementById('calculateBtn');
const results = document.getElementById('results');
const scaledRecipe = document.getElementById('scaledRecipe');
const displayUnit = document.getElementById('displayUnit');

// Event listeners
recipeSelect.addEventListener('change', handleRecipeChange);
calculateBtn.addEventListener('click', calculateRecipe);
displayUnit.addEventListener('change', updateResults);
baseIngredient.addEventListener('change', updateUnits);

function handleRecipeChange() {
    const selectedRecipe = recipeSelect.value;
    if (selectedRecipe && recipes[selectedRecipe]) {
        currentRecipe = recipes[selectedRecipe];
        showRecipeDetails();
    } else {
        recipeDetails.classList.add('hidden');
        results.classList.add('hidden');
    }
}

function showRecipeDetails() {
    recipeDetails.classList.remove('hidden');
    displayBaseRecipe();
    populateBaseIngredients();
    results.classList.add('hidden');
}

function displayBaseRecipe() {
    baseRecipe.innerHTML = '';
    Object.entries(currentRecipe.ingredients).forEach(([key, ingredient]) => {
        const card = createIngredientCard(formatIngredientName(key), ingredient.amount, ingredient.unit);
        baseRecipe.appendChild(card);
    });
}

function populateBaseIngredients() {
    baseIngredient.innerHTML = '';
    Object.entries(currentRecipe.ingredients).forEach(([key, ingredient]) => {
        const option = document.createElement('option');
        option.value = key;
        option.textContent = formatIngredientName(key);
        baseIngredient.appendChild(option);
    });
    updateUnits();
}

function updateUnits() {
    const selectedIngredient = baseIngredient.value;
    if (!selectedIngredient || !currentRecipe) return;
    
    const ingredient = currentRecipe.ingredients[selectedIngredient];
    desiredUnit.innerHTML = '';
    
    let units = [];
    if (ingredient.type === 'weight') {
        units = ['g', 'kg', 'oz', 'lb'];
    } else if (ingredient.type === 'volume') {
        units = ['ml', 'l', 'tsp', 'tbsp', 'cups', 'qt'];
    } else {
        units = [ingredient.unit];
    }
    
    units.forEach(unit => {
        const option = document.createElement('option');
        option.value = unit;
        option.textContent = unit;
        if (unit === ingredient.unit) option.selected = true;
        desiredUnit.appendChild(option);
    });
}

function calculateRecipe() {
    const selectedIngredient = baseIngredient.value;
    const amount = parseFloat(desiredAmount.value);
    const unit = desiredUnit.value;
    
    if (!selectedIngredient || !amount || !unit) {
        alert('Please fill in all fields');
        return;
    }
    
    const baseIngredientData = currentRecipe.ingredients[selectedIngredient];
    
    // Convert both amounts to the same base unit for comparison
    const baseAmountInBaseUnit = convertToBaseUnit(baseIngredientData.amount, baseIngredientData.unit, baseIngredientData.type);
    const desiredAmountInBaseUnit = convertToBaseUnit(amount, unit, baseIngredientData.type);
    
    scaleFactor = desiredAmountInBaseUnit / baseAmountInBaseUnit;
    
    updateResults();
    results.classList.remove('hidden');
}

function convertToBaseUnit(amount, unit, type) {
    if (type === 'weight') {
        return amount * (conversions.weight[unit] || 1);
    } else if (type === 'volume') {
        return amount * (conversions.volume[unit] || 1);
    }
    return amount;
}

function convertFromBaseUnit(amount, targetUnit, type) {
    if (type === 'weight') {
        return amount / (conversions.weight[targetUnit] || 1);
    } else if (type === 'volume') {
        return amount / (conversions.volume[targetUnit] || 1);
    }
    return amount;
}

function updateResults() {
    if (!currentRecipe || scaleFactor === 1) return;
    
    scaledRecipe.innerHTML = '';
    const displaySystem = displayUnit.value;
    
    Object.entries(currentRecipe.ingredients).forEach(([key, ingredient]) => {
        const scaledAmount = ingredient.amount * scaleFactor;
        const displayInfo = getDisplayUnit(scaledAmount, ingredient.unit, ingredient.type, displaySystem);
        
        const card = createIngredientCard(
            formatIngredientName(key), 
            displayInfo.amount, 
            displayInfo.unit,
            true
        );
        scaledRecipe.appendChild(card);
    });
}

function getDisplayUnit(amount, originalUnit, type, system) {
    if (system === 'mixed' || type === 'count') {
        return { amount: formatNumber(amount), unit: originalUnit };
    }
    
    const baseAmount = convertToBaseUnit(amount, originalUnit, type);
    
    if (type === 'weight') {
        const units = displayUnits[system].weight;
        if (baseAmount >= units.threshold) {
            return {
                amount: formatNumber(convertFromBaseUnit(baseAmount, units.large, type)),
                unit: units.large
            };
        } else {
            return {
                amount: formatNumber(convertFromBaseUnit(baseAmount, units.small, type)),
                unit: units.small
            };
        }
    } else if (type === 'volume' && system === 'imperial') {
        const units = displayUnits.imperial.volume;
        const tspAmount = convertFromBaseUnit(baseAmount, 'tsp', type);
        
        if (tspAmount >= units.thresholds[1]) {
            return {
                amount: formatNumber(convertFromBaseUnit(baseAmount, units.large, type)),
                unit: units.large
            };
        } else if (tspAmount >= units.thresholds[0]) {
            return {
                amount: formatNumber(convertFromBaseUnit(baseAmount, units.medium, type)),
                unit: units.medium
            };
        } else {
            return {
                amount: formatNumber(tspAmount),
                unit: units.small
            };
        }
    } else if (type === 'volume') {
        const units = displayUnits.metric.volume;
        if (baseAmount >= units.threshold) {
            return {
                amount: formatNumber(convertFromBaseUnit(baseAmount, units.large, type)),
                unit: units.large
            };
        } else {
            return {
                amount: formatNumber(convertFromBaseUnit(baseAmount, units.small, type)),
                unit: units.small
            };
        }
    }
    
    return { amount: formatNumber(amount), unit: originalUnit };
}

function createIngredientCard(name, amount, unit, isScaled = false) {
    const card = document.createElement('div');
    card.className = `p-4 border rounded-lg ${isScaled ? 'bg-primary-50 border-primary-200' : 'bg-gray-50 border-gray-200'}`;
    
    card.innerHTML = `
        <div class="font-medium text-gray-900 mb-1">${name}</div>
        <div class="text-lg font-semibold ${isScaled ? 'text-primary-600' : 'text-gray-700'}">
            ${amount} ${unit}
        </div>
    `;
    
    return card;
}

function formatIngredientName(key) {
    return key.replace(/([A-Z])/g, ' $1')
              .replace(/^./, str => str.toUpperCase())
              .trim();
}

function formatNumber(num) {
    if (num % 1 === 0) return num.toString();
    if (num < 1) return num.toFixed(2).replace(/\\.?0+$/, '');
    return num.toFixed(1).replace(/\\.?0+$/, '');
}

// Initialize the app
document.addEventListener('DOMContentLoaded', function() {
    // Set default values
    displayUnit.value = 'mixed';
});'''

with open('script.js', 'w') as f:
    f.write(js_content)