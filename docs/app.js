/**
 * Rune Codex - Enterprise Catalog UI
 */

const STATE = {
  items: [],
  filtered: [],
  search: '',
  platform: 'all',
  type: 'all',
  area: 'all',
  status: 'all',
  activeItem: null
};

// Color mapping per domain
const AREA_COLORS = {
  'engineering': '#3b82f6',
  'devops': '#06b6d4',
  'database': '#8b5cf6',
  'security': '#ef4444',
  'data-ai': '#10b981',
  'qa': '#f59e0b',
  'product': '#ec4899',
  'design-ux': '#f43f5e',
  'content': '#14b8a6',
  'sales': '#84cc16',
  'customer-success': '#0ea5e9',
  'marketing': '#d946ef',
  'business': '#6366f1',
  'finance': '#eab308',
  'hr': '#22c55e',
  'legal': '#94a3b8'
};

// DOM Elements
const searchInput = document.getElementById('searchInput');
const clearSearchBtn = document.getElementById('clearSearchBtn');
const platformPills = document.querySelectorAll('#platformFilter .pill');
const typePills = document.querySelectorAll('#typeFilter .pill');
const areaSelect = document.getElementById('areaSelect');
const statusSelect = document.getElementById('statusSelect');
const resultsCount = document.getElementById('resultsCount');
const totalCount = document.getElementById('totalCount');
const resetFiltersBtn = document.getElementById('resetFiltersBtn');
const cardsGrid = document.getElementById('cardsGrid');

// Modal Elements
const detailModal = document.getElementById('detailModal');
const modalCloseBtn = document.getElementById('modalCloseBtn');
const modalTitle = document.getElementById('modalTitle');
const modalDescription = document.getElementById('modalDescription');
const modalBadges = document.getElementById('modalBadges');
const modalMetaGrid = document.getElementById('modalMetaGrid');
const modalCode = document.getElementById('modalCode');
const modalInstallCmd = document.getElementById('modalInstallCmd');
const copyPayloadBtn = document.getElementById('copyPayloadBtn');
const copyInstallBtn = document.getElementById('copyInstallBtn');
const payloadTitle = document.getElementById('payloadTitle');
const toastContainer = document.getElementById('toastContainer');

/**
 * Initialize application
 */
async function init() {
  setupEventListeners();
  await loadCatalogData();
  render();
}

/**
 * Load index data from potential static locations
 */
async function loadCatalogData() {
  const possiblePaths = [
    './data/index.json',
    '../catalog/index.json',
    './catalog/index.json',
    './index.json'
  ];

  for (const path of possiblePaths) {
    try {
      const resp = await fetch(path);
      if (resp.ok) {
        STATE.items = await resp.json();
        totalCount.textContent = STATE.items.length;
        console.log(`Loaded ${STATE.items.length} items from ${path}`);
        return;
      }
    } catch (e) {
      // Try next path
    }
  }

  cardsGrid.innerHTML = `
    <div class="empty-state">
      <h3>Failed to load catalog index</h3>
      <p>Please make sure <code>catalog/index.json</code> exists or run <code>python3 scripts/generate_index.py</code>.</p>
    </div>
  `;
}

/**
 * Setup DOM event listeners
 */
function setupEventListeners() {
  // Search input
  searchInput.addEventListener('input', (e) => {
    STATE.search = e.target.value.trim().toLowerCase();
    clearSearchBtn.style.display = STATE.search ? 'flex' : 'none';
    applyFilters();
  });

  clearSearchBtn.addEventListener('click', () => {
    searchInput.value = '';
    STATE.search = '';
    clearSearchBtn.style.display = 'none';
    searchInput.focus();
    applyFilters();
  });

  // Platform filters
  platformPills.forEach(pill => {
    pill.addEventListener('click', () => {
      platformPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      STATE.platform = pill.dataset.value;
      applyFilters();
    });
  });

  // Type filters
  typePills.forEach(pill => {
    pill.addEventListener('click', () => {
      typePills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      STATE.type = pill.dataset.value;
      applyFilters();
    });
  });

  // Select filters
  areaSelect.addEventListener('change', (e) => {
    STATE.area = e.target.value;
    applyFilters();
  });

  statusSelect.addEventListener('change', (e) => {
    STATE.status = e.target.value;
    applyFilters();
  });

  // Reset filters
  resetFiltersBtn.addEventListener('click', resetAllFilters);

  // Modal interactions
  modalCloseBtn.addEventListener('click', closeModal);
  detailModal.addEventListener('click', (e) => {
    if (e.target === detailModal) closeModal();
  });

  // Keyboard shortcuts
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && detailModal.style.display !== 'none') {
      closeModal();
    }
    if (e.key === '/' && document.activeElement !== searchInput && detailModal.style.display === 'none') {
      e.preventDefault();
      searchInput.focus();
    }
  });

  // Copy buttons
  copyPayloadBtn.addEventListener('click', () => {
    if (!STATE.activeItem) return;
    const contentToCopy = extractCleanPayload(STATE.activeItem);
    navigator.clipboard.writeText(contentToCopy).then(() => {
      showToast('Payload copied to clipboard!');
    });
  });

  copyInstallBtn.addEventListener('click', () => {
    if (!STATE.activeItem) return;
    const cmd = getInstallCommand(STATE.activeItem);
    navigator.clipboard.writeText(cmd).then(() => {
      showToast('Install command copied to clipboard!');
    });
  });
}

/**
 * Filter catalog items
 */
function applyFilters() {
  const q = STATE.search;
  
  STATE.filtered = STATE.items.filter(item => {
    // Platform match
    if (STATE.platform !== 'all' && item.platform !== STATE.platform) {
      return false;
    }

    // Type match
    if (STATE.type !== 'all' && item.type !== STATE.type) {
      return false;
    }

    // Area match
    if (STATE.area !== 'all' && item.area !== STATE.area) {
      return false;
    }

    // Status match
    if (STATE.status !== 'all' && item.status !== STATE.status) {
      return false;
    }

    // Search query match
    if (q) {
      const matchName = item.name.toLowerCase().includes(q);
      const matchDesc = (item.description || '').toLowerCase().includes(q);
      const matchArea = (item.area || '').toLowerCase().includes(q);
      const matchType = (item.type || '').toLowerCase().includes(q);
      const matchContent = (item.content || '').toLowerCase().includes(q);
      if (!matchName && !matchDesc && !matchArea && !matchType && !matchContent) {
        return false;
      }
    }

    return true;
  });

  render();
}

/**
 * Reset all active filters
 */
function resetAllFilters() {
  STATE.search = '';
  STATE.platform = 'all';
  STATE.type = 'all';
  STATE.area = 'all';
  STATE.status = 'all';

  searchInput.value = '';
  clearSearchBtn.style.display = 'none';

  platformPills.forEach(p => p.classList.toggle('active', p.dataset.value === 'all'));
  typePills.forEach(p => p.classList.toggle('active', p.dataset.value === 'all'));
  areaSelect.value = 'all';
  statusSelect.value = 'all';

  applyFilters();
}

/**
 * Render cards and results count
 */
function render() {
  const total = STATE.items.length;
  const count = STATE.filtered.length;

  resultsCount.textContent = `Showing ${count} of ${total} items`;

  const isFiltered = STATE.search || STATE.platform !== 'all' || STATE.type !== 'all' || STATE.area !== 'all' || STATE.status !== 'all';
  resetFiltersBtn.style.display = isFiltered ? 'inline-block' : 'none';

  if (count === 0) {
    cardsGrid.innerHTML = `
      <div class="empty-state">
        <h3>No matching catalog items found</h3>
        <p>Try adjusting your search query or reset filters.</p>
      </div>
    `;
    return;
  }

  const html = STATE.filtered.map(item => {
    const areaColor = AREA_COLORS[item.area] || '#6366f1';
    const statusClass = item.status === 'production' ? 'production' : 'experimental';
    const cleanTitle = item.name.replace(/-/g, ' ');

    return `
      <div class="catalog-card" style="--card-accent-color: ${areaColor}" onclick="openItemDetail('${item.id}')">
        <div class="card-top">
          <div class="badges-row">
            <span class="badge-area">${item.area}</span>
            <span class="badge-platform">${item.platform}</span>
            <span class="badge-type">${item.type}</span>
          </div>
          <span class="badge-status ${statusClass}">${item.status}</span>
        </div>

        <h3 class="card-title">${cleanTitle}</h3>
        <p class="card-description">${escapeHtml(item.description || 'No description provided.')}</p>

        <div class="card-footer">
          <span class="card-model">${item.model ? `model: ${item.model}` : item.tools ? `${item.tools.length} tools` : ''}</span>
          <div class="card-actions">
            <button class="btn btn-sm btn-outline" onclick="event.stopPropagation(); quickCopy('${item.id}')">Copy</button>
            <button class="btn btn-sm btn-ghost" onclick="event.stopPropagation(); openItemDetail('${item.id}')">View</button>
          </div>
        </div>
      </div>
    `;
  }).join('');

  cardsGrid.innerHTML = html;
}

/**
 * Open item detail modal
 */
function openItemDetail(itemId) {
  const item = STATE.items.find(i => i.id === itemId);
  if (!item) return;

  STATE.activeItem = item;
  const areaColor = AREA_COLORS[item.area] || '#6366f1';

  modalTitle.textContent = item.name.replace(/-/g, ' ');
  modalDescription.textContent = item.description || '';

  modalBadges.innerHTML = `
    <span class="badge-area" style="--card-accent-color: ${areaColor}; color: ${areaColor}">${item.area}</span>
    <span class="badge-platform">${item.platform}</span>
    <span class="badge-type">${item.type}</span>
    <span class="badge-status ${item.status === 'production' ? 'production' : 'experimental'}">${item.status}</span>
  `;

  modalMetaGrid.innerHTML = `
    <div class="meta-item">
      <span class="meta-key">Relative File</span>
      <span class="meta-val">${item.file}</span>
    </div>
    <div class="meta-item">
      <span class="meta-key">Status Note / Context</span>
      <span class="meta-val">${escapeHtml(item.context || 'None')}</span>
    </div>
    ${item.model ? `
      <div class="meta-item">
        <span class="meta-key">Target Model</span>
        <span class="meta-val">${item.model}</span>
      </div>
    ` : ''}
    ${item.tools ? `
      <div class="meta-item">
        <span class="meta-key">Pre-wired Tools</span>
        <span class="meta-val">${Array.isArray(item.tools) ? item.tools.join(', ') : item.tools}</span>
      </div>
    ` : ''}
  `;

  // Payload / instructions
  if (item.type === 'mcp') {
    payloadTitle.textContent = 'MCP Server Configuration (JSON)';
  } else if (item.type === 'skills') {
    payloadTitle.textContent = 'Skill Instructions / Template';
  } else {
    payloadTitle.textContent = 'Prompt / Instructions';
  }

  const payload = extractCleanPayload(item);
  modalCode.textContent = payload;

  const installCmd = getInstallCommand(item);
  modalInstallCmd.textContent = installCmd;

  detailModal.style.display = 'flex';
}

/**
 * Close detail modal
 */
function closeModal() {
  detailModal.style.display = 'none';
  STATE.activeItem = null;
}

/**
 * Extract clean prompt / configuration from item content
 */
function extractCleanPayload(item) {
  if (!item.content) return '';

  // Extract from fenced code block if present
  const match = item.content.match(/```(?:\w+)?\n([\s\S]*?)\n```/);
  if (match) {
    return match[1].trim();
  }

  return item.content.trim();
}

/**
 * Generate install command for item
 */
function getInstallCommand(item) {
  return `python3 scripts/install.py ${item.file}`;
}

/**
 * Quick copy from card
 */
function quickCopy(itemId) {
  const item = STATE.items.find(i => i.id === itemId);
  if (!item) return;

  const payload = extractCleanPayload(item);
  navigator.clipboard.writeText(payload).then(() => {
    showToast(`Copied ${item.name} prompt!`);
  });
}

/**
 * Show toast notification
 */
function showToast(message) {
  const toast = document.createElement('div');
  toast.className = 'toast';
  toast.textContent = message;
  toastContainer.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transition = 'opacity 0.3s ease';
    setTimeout(() => toast.remove(), 300);
  }, 2500);
}

/**
 * Helper to escape HTML characters
 */
function escapeHtml(str) {
  if (!str) return '';
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

// Start application
window.addEventListener('DOMContentLoaded', init);
