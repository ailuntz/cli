#!/usr/bin/env node

/**
 * Ailuntz Personal CV CLI Tool
 */

// ANSI color codes
const colors = {
  reset: '\x1b[0m',
  bold: '\x1b[1m',
  cyan: '\x1b[96m',
  magenta: '\x1b[95m',
  yellow: '\x1b[93m',
  green: '\x1b[92m',
  blue: '\x1b[94m',
  red: '\x1b[91m',
};

function printCV() {
  const border = '═'.repeat(60);

  const cvContent = `
${colors.cyan}${colors.bold}${border}${colors.reset}
${colors.cyan}${colors.bold}                    ✨ AILUNTZ - CV ✨${colors.reset}
${colors.cyan}${colors.bold}${border}${colors.reset}

${colors.magenta}${colors.bold}👤 Name:${colors.reset}          ${colors.yellow}Ailuntz${colors.reset}
${colors.magenta}${colors.bold}💼 Title:${colors.reset}         ${colors.yellow}Full Stack Developer${colors.reset}
${colors.magenta}${colors.bold}📍 Location:${colors.reset}      ${colors.yellow}China${colors.reset}
${colors.magenta}${colors.bold}📧 Email:${colors.reset}         ${colors.yellow}ailuntz@icloud.com${colors.reset}
${colors.magenta}${colors.bold}🔗 Website:${colors.reset}       ${colors.yellow}https://ailuntz.com${colors.reset}

${colors.cyan}${colors.bold}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${colors.reset}

${colors.green}${colors.bold}💻 SKILLS${colors.reset}
  ${colors.blue}•${colors.reset} Languages:     Python, JavaScript, TypeScript, Go
  ${colors.blue}•${colors.reset} Frontend:      React, Vue.js, Next.js, Tailwind CSS
  ${colors.blue}•${colors.reset} Backend:       Node.js, Django, FastAPI, Express
  ${colors.blue}•${colors.reset} Database:      PostgreSQL, MongoDB, Redis
  ${colors.blue}•${colors.reset} DevOps:        Docker, Kubernetes, CI/CD, AWS
  ${colors.blue}•${colors.reset} Tools:         Git, Linux, Nginx, Vim

${colors.cyan}${colors.bold}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${colors.reset}

${colors.green}${colors.bold}🎓 EDUCATION${colors.reset}
  ${colors.blue}•${colors.reset} Computer Science & Technology
  ${colors.blue}•${colors.reset} Focus on Software Engineering & AI

${colors.cyan}${colors.bold}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${colors.reset}

${colors.green}${colors.bold}🚀 PROJECTS${colors.reset}
  ${colors.blue}•${colors.reset} CLI Tools:     Personal command-line utilities
  ${colors.blue}•${colors.reset} Web Apps:      Full-stack web applications
  ${colors.blue}•${colors.reset} Open Source:   Contributing to various projects

${colors.cyan}${colors.bold}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${colors.reset}

${colors.red}${colors.bold}💡 INTERESTS${colors.reset}
  ${colors.blue}•${colors.reset} AI & Machine Learning
  ${colors.blue}•${colors.reset} System Design & Architecture
  ${colors.blue}•${colors.reset} Developer Tools & CLI Applications
  ${colors.blue}•${colors.reset} Open Source Community

${colors.cyan}${colors.bold}${border}${colors.reset}
${colors.cyan}${colors.bold}            💌 Thanks for checking out my CV!${colors.reset}
${colors.cyan}${colors.bold}${border}${colors.reset}
`;

  console.log(cvContent);
}

// Main execution
function main() {
  const args = process.argv.slice(2);
  const command = args[0];

  if (!command || command === 'cv') {
    try {
      printCV();
      process.exit(0);
    } catch (error) {
      console.error('Error:', error.message);
      process.exit(1);
    }
  } else if (command === '--help' || command === '-h') {
    console.log(`
${colors.cyan}${colors.bold}Ailuntz CLI - Personal CV Tool${colors.reset}

Usage:
  ${colors.green}ailuntz cv${colors.reset}      Display CV
  ${colors.green}ailuntz --help${colors.reset}  Show this help message

Examples:
  ${colors.yellow}ailuntz cv${colors.reset}
    `);
    process.exit(0);
  } else {
    console.error(`${colors.red}Unknown command: ${command}${colors.reset}`);
    console.log(`Run ${colors.green}ailuntz --help${colors.reset} for usage information.`);
    process.exit(1);
  }
}

// Handle keyboard interrupt
process.on('SIGINT', () => {
  console.log('\n\nGoodbye! 👋');
  process.exit(0);
});

main();
