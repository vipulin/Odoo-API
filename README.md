<section class="oe_container">
    <div class="oe_row oe_spaced">
        <div class="oe_span12">
            <h3 class="oe_slogan">1. Install Module</h3>
        </div>
	      <div class="oe_span6">
            <p class="oe_mt32">
		          Login with authorized user for module installation -> update module list -> find 'products_api' module -> install.
            </p>
            <p class="oe_mt32">
		          Once module installation will completed automatic one user will create with api_key 91906b00204711eb9d622c6e856ebaef. 
            </p>
            <p class="oe_mt32">
		          If you want create new user:
            </p>
            <p class="oe_mt32">
		          Click on: Settings -> Users & Companies -> Users. Now create user with mandatory details and click on API tab -> Generate Api Key. Now you can use Api Key (Access rights need to manage for product read)
            </p>
        </div>
    </div>
</section>
<section class="oe_container">
    <div class="oe_row oe_spaced">
        <div class="oe_span12">
            <h3 class="oe_slogan">2. Create Product</h3>
        </div>
	      <div class="oe_span6">
            <p class="oe_mt32">
		          Click on: Inventory -> Master Data -> Products. Now create product with mandatory details.
            </p>
        </div>
    </div>
</section>
<section class="oe_container">
    <div class="oe_row oe_spaced">
        <div class="oe_span12">
            <h3 class="oe_slogan">3. Call API Using Postman</h3>
        </div>
	      <div class="oe_span6">
            <p class="oe_mt32">
		          Add URL with GET method: http://[domain]/api/v1/product/[product_id:int]. Example: http://localhost:8069/api/v1/product/1
            </p>
            <p class="oe_mt32">
		          Add following headers: Content-Type:application/json; api_key:91906b00204711eb9d622c6e856ebaef
            </p>
            <p class="oe_mt32">
		          Add body type raw: {"jsonrpc": "2.0",
                "method": "call",
                "params": {},
                "id": null}
            </p>
            <p class="oe_mt32">
		          Click on Send.
            </p>
            <p class="oe_mt32">
              <h5>Response<h5>
            </p>
            <p class="oe_mt32">
		           {
                  "jsonrpc": "2.0",
                  "id": null,
                  "result": {
                      "id": 1,
                      "name": "Test",
                      "list_price": 600.0,
                      "standard_price": 500.0,
                      "qty_available": 10.0,
                      "categ_id": [
                          1,
                          "All"
                      ]
                  }
              }
            </p>
        </div>
    </div>
</section>
