// tailwind.config.js
module.exports = {
  content: [
    './**/templates/**/*.html',
    './**/static/js/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        green: {
          700: '#047857',
          800: '#065F46',
        },
      },
    },
  },
  plugins: [],
}
