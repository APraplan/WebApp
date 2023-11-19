fetch('static/settings.json')
  .then(response => response.json())
  .then(data => {

    document.documentElement.style.setProperty('--text-color', data.colors.text);
    document.documentElement.style.setProperty('--hover-color', data.colors.hover);
    document.documentElement.style.setProperty('--accent-color', data.colors.accent);
    document.documentElement.style.setProperty('--blurred-color', data.colors.blurred);

    document.documentElement.style.setProperty('--small-font-size', data.fontSizes.small);
    document.documentElement.style.setProperty('--medium-font-size', data.fontSizes.medium);
    document.documentElement.style.setProperty('--large-font-size', data.fontSizes.large);
    document.documentElement.style.setProperty('--menuBar-Height', data.menuBarHeight);
  })
  .catch(error => console.error('Error loading settings:', error));