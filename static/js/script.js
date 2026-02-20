

let selectedOption = null;
let promptText = '';

// Step 1: save option, go to step 2
const optionCards = document.querySelectorAll('.option-card');
optionCards.forEach(card => {
    card.addEventListener('click', () => {
        optionCards.forEach(c => c.classList.remove('selected'));
        card.classList.add('selected');
        selectedOption = card.dataset.value;  
        setTimeout(() => { goToStep(2); }, 300);
    });
});

// Step 2: save prompt, send BOTH, then go to step 3
const skipBtn = document.getElementById('skipBtn');
const submitBtn = document.getElementById('submitBtn');

skipBtn.addEventListener('click', () => {
    promptText = '';                         
    sendBothAndLoadArticles();
});

submitBtn.addEventListener('click', () => {
    promptText = document.getElementById('promptInput').value.trim();
    sendBothAndLoadArticles();
});

// Send both option + prompt to Flask, receive articles, display them
function sendBothAndLoadArticles() {
    goToStep(3);

    // Show loading while waiting for Flask
    document.querySelector('.articles-header h1').textContent = 'Loading News...';
    document.getElementById('articlesContainer').innerHTML = '<p style="padding:2rem">Loading...</p>';

    fetch('/api/generate', {                  
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({              
            option: selectedOption,
            prompt: promptText
        })
    })
    .then(response => response.json())        // parse Flask's response
    .then(result => {
        if (result.status === 'error') {   
            document.querySelector('.articles-header h1').textContent = 'Latest News';
            document.getElementById('articlesContainer').innerHTML = '<p style="padding: 2.5rem; text-align: center; color: var(--ink-muted);">Something went wrong. Please try again.</p>';
            return;
        }
        displayArticles(result.articles);     // result is what Flask returns
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('articlesContainer').innerHTML = '<p style="padding:2rem">Something went wrong.</p>';
    });
}

// Take articles array from Flask and build the HTML
function displayArticles(articles) {
    document.querySelector('.articles-header h1').textContent = 'Latest News';
    const container = document.getElementById('articlesContainer');
    if (!articles || articles.length === 0) {
        container.innerHTML = '<p style="padding: 2.5rem; text-align: center; color: var(--ink-muted);">No suitable articles found.</p>';
        return;
    }
    container.innerHTML = articles.map((article, index) => `
        <article class="article-section" style="animation-delay: ${index * 0.1}s">
            <div class="article-meta">
                <span class="article-author">${article.author}</span>
                <span class="article-date">${article.publishedAt}</span>
            </div>
            <h2 class="article-title">${article.title}</h2>
            <div class="article-content">${article.summary}</div>
            <a href="${article.url}" class="article-link" target="_blank">Read full article</a>
        </article>
    `).join('');
}

// Step navigation (unchanged)
function goToStep(stepNumber) {
    document.querySelectorAll('.step').forEach(step => step.classList.remove('active'));
    document.getElementById(`step${stepNumber}`).classList.add('active');
    const progressBar = document.querySelector('.progress');
    if (stepNumber === 3) {
        progressBar.style.display = 'none';
    } else {
        progressBar.style.display = 'flex';
        document.querySelectorAll('.progress-dot').forEach((dot, index) => {
            dot.classList.toggle('active', index === stepNumber - 1);
        });
    }
}
