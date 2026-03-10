// ZINWA HR Dashboard - JavaScript
// NO IMPORTS - This is a standalone HTML file that uses Chart.js from CDN

// JSON Data Structure - Replace with backend data later
var hrData = {
    summary: {
        totalEmployees: 1247,
        permanentStaff: 892,
        contractStaff: 355,
        maleCount: 723,
        femaleCount: 524
    },
    catchments: [
        { name: "Head Office", total: 187, permanent: 156, contract: 31, male: 98, female: 89 },
        { name: "Save", total: 156, permanent: 112, contract: 44, male: 92, female: 64 },
        { name: "Sanyati", total: 143, permanent: 98, contract: 45, male: 85, female: 58 },
        { name: "Runde", total: 168, permanent: 124, contract: 44, male: 102, female: 66 },
        { name: "Mazowe", total: 178, permanent: 138, contract: 40, male: 108, female: 70 },
        { name: "Manyame", total: 162, permanent: 118, contract: 44, male: 94, female: 68 },
        { name: "Gwayi", total: 134, permanent: 92, contract: 42, male: 78, female: 56 },
        { name: "Mzingwane", total: 119, permanent: 54, contract: 65, male: 66, female: 53 }
    ],
    monthlyGrowth: [
        { month: "Jan", count: 1180 },
        { month: "Feb", count: 1185 },
        { month: "Mar", count: 1192 },
        { month: "Apr", count: 1198 },
        { month: "May", count: 1210 },
        { month: "Jun", count: 1218 },
        { month: "Jul", count: 1225 },
        { month: "Aug", count: 1232 },
        { month: "Sep", count: 1238 },
        { month: "Oct", count: 1240 },
        { month: "Nov", count: 1244 },
        { month: "Dec", count: 1247 }
    ],
    monthlyHiring: [
        { month: "Jan", hired: 12 },
        { month: "Feb", hired: 8 },
        { month: "Mar", hired: 15 },
        { month: "Apr", hired: 10 },
        { month: "May", hired: 18 },
        { month: "Jun", hired: 14 },
        { month: "Jul", hired: 11 },
        { month: "Aug", hired: 16 },
        { month: "Sep", hired: 9 },
        { month: "Oct", hired: 7 },
        { month: "Nov", hired: 13 },
        { month: "Dec", hired: 6 }
    ]
};

// Color palette for charts (water-themed blues)
var chartColors = {
    primary: '#0066b3',
    primaryLight: '#0088cc',
    accent: '#00b4d8',
    accentLight: '#48cae4',
    catchments: [
        '#0052a3',
        '#0066b3',
        '#0088cc',
        '#00b4d8',
        '#48cae4',
        '#90e0ef',
        '#ade8f4',
        '#caf0f8'
    ]
};

// Initialize Dashboard when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    initializeCharts();
    populateTable();
    updateStatCards();
    setupEventListeners();
});

// Setup Event Listeners
function setupEventListeners() {
    // Sidebar toggle
    var menuToggle = document.getElementById('menuToggle');
    if (menuToggle) {
        menuToggle.addEventListener('click', toggleSidebar);
    }
    
    // Dropdown toggle - attach to all dropdown toggles
    var dropdownToggles = document.querySelectorAll('.dropdown-toggle');
    dropdownToggles.forEach(function(toggle) {
        toggle.addEventListener('click', function(e) {
            e.preventDefault();
            var navItem = this.closest('.nav-item.has-dropdown');
            if (navItem) {
                navItem.classList.toggle('open');
            }
        });
    });
    
    // Export button
    var exportBtn = document.getElementById('exportBtn');
    if (exportBtn) {
        exportBtn.addEventListener('click', function() {
            alert('Export functionality will be connected to backend');
        });
    }
}

// Toggle Sidebar
function toggleSidebar() {
    var sidebar = document.getElementById('sidebar');
    if (sidebar) {
        sidebar.classList.toggle('open');
        sidebar.classList.toggle('collapsed');
    }
}

// Update Stat Cards
function updateStatCards() {
    var summary = hrData.summary;
    
    var totalEl = document.getElementById('totalEmployees');
    var permanentEl = document.getElementById('permanentStaff');
    var contractEl = document.getElementById('contractStaff');
    var genderEl = document.getElementById('genderRatio');
    
    if (totalEl) totalEl.textContent = summary.totalEmployees.toLocaleString();
    if (permanentEl) permanentEl.textContent = summary.permanentStaff.toLocaleString();
    if (contractEl) contractEl.textContent = summary.contractStaff.toLocaleString();
    
    if (genderEl) {
        var malePercent = Math.round((summary.maleCount / summary.totalEmployees) * 100);
        var femalePercent = 100 - malePercent;
        genderEl.textContent = malePercent + '% / ' + femalePercent + '%';
    }
}

// Initialize All Charts
function initializeCharts() {
    createGrowthChart();
    createCatchmentChart();
    createGenderChart();
    createEmploymentChart();
    createHiringChart();
}

// Employee Growth Line Chart
function createGrowthChart() {
    var canvas = document.getElementById('growthChart');
    if (!canvas) return;
    
    var ctx = canvas.getContext('2d');
    
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: hrData.monthlyGrowth.map(function(d) { return d.month; }),
            datasets: [{
                label: 'Total Employees',
                data: hrData.monthlyGrowth.map(function(d) { return d.count; }),
                borderColor: chartColors.accent,
                backgroundColor: 'rgba(0, 180, 216, 0.1)',
                fill: true,
                tension: 0.4,
                pointBackgroundColor: chartColors.accent,
                pointBorderColor: '#fff',
                pointBorderWidth: 2,
                pointRadius: 4,
                pointHoverRadius: 6
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    backgroundColor: '#1e293b',
                    titleColor: '#fff',
                    bodyColor: '#fff',
                    padding: 12,
                    cornerRadius: 8
                }
            },
            scales: {
                x: {
                    grid: {
                        display: false
                    },
                    ticks: {
                        color: '#94a3b8'
                    }
                },
                y: {
                    beginAtZero: false,
                    min: 1150,
                    grid: {
                        color: '#e2e8f0',
                        drawBorder: false
                    },
                    ticks: {
                        color: '#94a3b8'
                    }
                }
            }
        }
    });
}

// Catchment Distribution Pie Chart
function createCatchmentChart() {
    var canvas = document.getElementById('catchmentChart');
    if (!canvas) return;
    
    var ctx = canvas.getContext('2d');
    
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: hrData.catchments.map(function(c) { return c.name; }),
            datasets: [{
                data: hrData.catchments.map(function(c) { return c.total; }),
                backgroundColor: chartColors.catchments,
                borderWidth: 0,
                hoverOffset: 4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'right',
                    labels: {
                        boxWidth: 12,
                        padding: 12,
                        font: {
                            size: 11
                        },
                        color: '#475569'
                    }
                },
                tooltip: {
                    backgroundColor: '#1e293b',
                    titleColor: '#fff',
                    bodyColor: '#fff',
                    padding: 12,
                    cornerRadius: 8,
                    callbacks: {
                        label: function(context) {
                            var total = context.dataset.data.reduce(function(a, b) { return a + b; }, 0);
                            var percentage = ((context.raw / total) * 100).toFixed(1);
                            return context.label + ': ' + context.raw + ' (' + percentage + '%)';
                        }
                    }
                }
            },
            cutout: '60%'
        }
    });
}

// Gender Distribution Doughnut Chart
function createGenderChart() {
    var canvas = document.getElementById('genderChart');
    if (!canvas) return;
    
    var ctx = canvas.getContext('2d');
    var summary = hrData.summary;
    
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Male', 'Female'],
            datasets: [{
                data: [summary.maleCount, summary.femaleCount],
                backgroundColor: [chartColors.primary, chartColors.accent],
                borderWidth: 0,
                hoverOffset: 4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        boxWidth: 12,
                        padding: 16,
                        font: {
                            size: 12
                        },
                        color: '#475569'
                    }
                },
                tooltip: {
                    backgroundColor: '#1e293b',
                    titleColor: '#fff',
                    bodyColor: '#fff',
                    padding: 12,
                    cornerRadius: 8
                }
            },
            cutout: '65%'
        }
    });
}

// Employment Type Doughnut Chart
function createEmploymentChart() {
    var canvas = document.getElementById('employmentChart');
    if (!canvas) return;
    
    var ctx = canvas.getContext('2d');
    var summary = hrData.summary;
    
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Permanent', 'Contract'],
            datasets: [{
                data: [summary.permanentStaff, summary.contractStaff],
                backgroundColor: [chartColors.primaryLight, chartColors.accentLight],
                borderWidth: 0,
                hoverOffset: 4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        boxWidth: 12,
                        padding: 16,
                        font: {
                            size: 12
                        },
                        color: '#475569'
                    }
                },
                tooltip: {
                    backgroundColor: '#1e293b',
                    titleColor: '#fff',
                    bodyColor: '#fff',
                    padding: 12,
                    cornerRadius: 8
                }
            },
            cutout: '65%'
        }
    });
}

// Monthly Hiring Bar Chart
function createHiringChart() {
    var canvas = document.getElementById('hiringChart');
    if (!canvas) return;
    
    var ctx = canvas.getContext('2d');
    
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: hrData.monthlyHiring.map(function(d) { return d.month; }),
            datasets: [{
                label: 'New Hires',
                data: hrData.monthlyHiring.map(function(d) { return d.hired; }),
                backgroundColor: chartColors.accent,
                borderRadius: 4,
                barThickness: 16
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    backgroundColor: '#1e293b',
                    titleColor: '#fff',
                    bodyColor: '#fff',
                    padding: 12,
                    cornerRadius: 8
                }
            },
            scales: {
                x: {
                    grid: {
                        display: false
                    },
                    ticks: {
                        color: '#94a3b8',
                        font: {
                            size: 10
                        }
                    }
                },
                y: {
                    beginAtZero: true,
                    grid: {
                        color: '#e2e8f0',
                        drawBorder: false
                    },
                    ticks: {
                        color: '#94a3b8',
                        stepSize: 5
                    }
                }
            }
        }
    });
}

// Populate Data Table
function populateTable() {
    var tbody = document.querySelector('#catchmentTable tbody');
    if (!tbody) return;
    
    tbody.innerHTML = '';
    
    hrData.catchments.forEach(function(catchment) {
        var row = document.createElement('tr');
        row.innerHTML = 
            '<td><strong>' + catchment.name + '</strong></td>' +
            '<td>' + catchment.total + '</td>' +
            '<td>' + catchment.permanent + '</td>' +
            '<td>' + catchment.contract + '</td>' +
            '<td>' + catchment.male + '</td>' +
            '<td>' + catchment.female + '</td>';
        tbody.appendChild(row);
    });
    
    // Add totals row
    var totalsRow = document.createElement('tr');
    totalsRow.style.background = '#f1f5f9';
    totalsRow.style.fontWeight = '600';
    totalsRow.innerHTML = 
        '<td><strong>Total</strong></td>' +
        '<td>' + hrData.summary.totalEmployees + '</td>' +
        '<td>' + hrData.summary.permanentStaff + '</td>' +
        '<td>' + hrData.summary.contractStaff + '</td>' +
        '<td>' + hrData.summary.maleCount + '</td>' +
        '<td>' + hrData.summary.femaleCount + '</td>';
    tbody.appendChild(totalsRow);
}

// Function to refresh data from backend (for future use)
function refreshDashboardData(newData) {
    if (newData) {
        Object.assign(hrData, newData);
        updateStatCards();
        populateTable();
    }
}

// Expose refresh function globally for external use
window.hrDashboard = {
    refreshData: refreshDashboardData,
    getData: function() { return hrData; }
};
