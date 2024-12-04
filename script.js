// Smooth Scrolling for Anchor Links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Dynamic Projects Fetching (if applicable)
const projectContainer = document.getElementById('project-container');
if (projectContainer) {
    fetch('/projects')
        .then(response => response.json())
        .then(data => {
            data.forEach(project => {
                const projectCard = document.createElement('div');
                projectCard.className = 'project-card';
                projectCard.innerHTML = `
                    <h3>${project.title}</h3>
                    <p>${project.description}</p>
                    <a href="${project.link}" target="_blank">View Project</a>
                `;
                projectContainer.appendChild(projectCard);
            });
        })
        .catch(error => console.error('Error fetching projects:', error));
}