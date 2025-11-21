#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');

// Paths (updated for .github/scripts location)
const yamlPath = path.join(__dirname, '../../api-reference/trails-api.gen.yaml');
const jsonPath = path.join(__dirname, '../../api-reference/trails-api.gen.json');

try {
  // Read YAML file
  const fileContents = fs.readFileSync(yamlPath, 'utf8');
  
  // Parse YAML to JS object
  const data = yaml.load(fileContents);
  
  // Convert to JSON and write to file
  fs.writeFileSync(jsonPath, JSON.stringify(data, null, 2));
  
  console.log(`✅ Successfully converted ${yamlPath} to ${jsonPath}`);
} catch (error) {
  console.error('❌ Error converting YAML to JSON:', error.message);
  process.exit(1);
}


