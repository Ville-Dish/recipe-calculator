// Recipe data structure
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
desiredAmount.addEventListener('input', validateForm);
desiredUnit.addEventListener('change', validateForm);

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
    validateForm(); // Check initial form state
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

    validateForm(); // Revalidate when units change
}

function validateForm() {
    const selectedIngredient = baseIngredient.value;
    const amount = desiredAmount.value.trim();
    const unit = desiredUnit.value;

    const isValid = selectedIngredient && amount && !isNaN(parseFloat(amount)) && parseFloat(amount) > 0 && unit;

    if (isValid) {
        calculateBtn.disabled = false;
        calculateBtn.classList.remove('opacity-50', 'cursor-not-allowed');
        calculateBtn.classList.add('hover:bg-primary-600');
    } else {
        calculateBtn.disabled = true;
        calculateBtn.classList.add('opacity-50', 'cursor-not-allowed');
        calculateBtn.classList.remove('hover:bg-primary-600');
    }

    return isValid;
}

function calculateRecipe() {
    if (!validateForm()) {
        return;
    }

    const selectedIngredient = baseIngredient.value;
    const amount = parseFloat(desiredAmount.value);
    const unit = desiredUnit.value;

    const baseIngredientData = currentRecipe.ingredients[selectedIngredient];

    // Convert both amounts to the same base unit for comparison
    const baseAmountInBaseUnit = convertToBaseUnit(baseIngredientData.amount, baseIngredientData.unit, baseIngredientData.type);
    const desiredAmountInBaseUnit = convertToBaseUnit(amount, unit, baseIngredientData.type);

    scaleFactor = desiredAmountInBaseUnit / baseAmountInBaseUnit;

    updateResults();
    results.classList.remove('hidden');

    // Scroll to results
    results.scrollIntoView({ behavior: 'smooth', block: 'start' });
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
    if (num < 1) return num.toFixed(2).replace(/\.?0+$/, '');
    return num.toFixed(1).replace(/\.?0+$/, '');
}

// Initialize the app
document.addEventListener('DOMContentLoaded', function() {
    // Set default values
    displayUnit.value = 'mixed';

    // Initialize button state
    validateForm();
});