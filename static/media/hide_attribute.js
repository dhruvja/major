document.addEventListener("DOMContentLoaded", function () {
  console.log("hellos");
  function toggleCity(value) {
    const cetWrapper = document.querySelector(".field-cet");
    const comedkWrapper = document.querySelector(".field-comedk");
    const managementWrapper = document.querySelector(".field-management");
    const diplomaWrapper = document.querySelector(".field-diploma");
    const cobWrapper = document.querySelector(".field-cob");
    console.log(value);
    if (value === "1") {
      cetWrapper.style.display = "block";
      comedkWrapper.style.display = "block";
      managementWrapper.style.display = "block";
      diplomaWrapper.style.display = "none";
      cobWrapper.style.display = "none";
    } else if (value === "3") {
      cetWrapper.style.display = "none";
      comedkWrapper.style.display = "none";
      managementWrapper.style.display = "none";
      diplomaWrapper.style.display = "block";
      cobWrapper.style.display = "block";
    } else {
      cetWrapper.style.display = "none";
      comedkWrapper.style.display = "none";
      managementWrapper.style.display = "none";
      diplomaWrapper.style.display = "none";
      cobWrapper.style.display = "none";
    }
  }

  function exportOnlySems(value) {
    const rows = document.querySelector("table#result_list")?.rows;
    if (!rows) {
      return;
    }

    Array.from(rows).forEach((row) => {
      if (
        row.innerHTML.includes('change/">3</a>') ||
        row.innerHTML.includes('change/">1</a>')
      ) {
        const input = row.cells[0].getElementsByTagName("input")[0];
        input.click();
      }
    });
  }

  const formatSelect = document.querySelector("select#id_semester");
  const actionSelect = document.querySelector("form#changelist-form select");
  if (formatSelect) {
    formatSelect.addEventListener("change", function () {
      toggleCity(this.value);
    });
  }
  actionSelect.addEventListener("change", function () {
    if (this.value === "export_admin_action") {
      exportOnlySems(this.value);
    }
  });
  console.log(actionSelect.value);
  toggleCity(formatSelect.value);
});
