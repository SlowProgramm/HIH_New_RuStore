// onboarding.js - Общие функции для onboarding

// Проверяем, проходил ли пользователь onboarding
function hasCompletedOnboarding() {
    return localStorage.getItem('onboardingCompleted') === 'true' || 
           getCookie('onboardingCompleted') === 'true';
}

// Устанавливаем флаг завершения onboarding
function setOnboardingCompleted() {
    localStorage.setItem('onboardingCompleted', 'true');
    setCookie('onboardingCompleted', 'true', 365); // На 1 год
}

// Функции для работы с cookies
function setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = `expires=${date.toUTCString()}`;
    document.cookie = `${name}=${value};${expires};path=/`;
}

function getCookie(name) {
    const nameEQ = name + "=";
    const ca = document.cookie.split(';');
    for(let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) === ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

// Запуск тура (переход со welcome на tour)
function startTour() {
    // Перенаправляем на страницу тура
    window.location.href = '/onboarding/tour/';
}

// Показ основного контента
function showMainContent() {
    const overlay = document.getElementById('onboardingOverlay');
    const mainContent = document.getElementById('mainContent');
    
    if (overlay) overlay.style.display = 'none';
    if (mainContent) mainContent.style.display = 'block';
}

// Инициализация при загрузке (для welcome страницы)
function initOnboarding() {
    if (hasCompletedOnboarding()) {
        showMainContent();
    }
}

// Автоматическая инициализация если на странице есть onboarding
if (document.getElementById('onboardingOverlay')) {
    document.addEventListener('DOMContentLoaded', initOnboarding);
}