/** @type {import('tailwindcss').Config} */
module.exports = {
  theme: {},
  variants: {},
  plugins: [],
  corePlugins: {},
  mode: 'jit',
  content: [
    // './pages/**/*.{html,js}',
    // './components/**/*.{html,js}',
    './dist/index.html'
  ],
  future: {
    removeDeprecatedGapUtilities: true,
    purgeLayersByDefault: true
  },
  experimental: {
    applyComplexClasses: true
  },
  output: {
    path: './dist/assets/css/main.css',
    sourceMap: true,
    publicPath: '/assets/css/main.css'
  }
}