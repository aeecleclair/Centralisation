/** @type {import('tailwindcss').Config} */

module.exports = {
  content: ["./src/**/*.{html,js}"],
  safelist: [
    "text-4xl",
    "leading-loose",
    "underline",
    "italic",
    "font-bold"
  ],
  theme: {
    extend: {
      colors: {
        'eclair': '#db6b02',
      },
    },
  },
}

